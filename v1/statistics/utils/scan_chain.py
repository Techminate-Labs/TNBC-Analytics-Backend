import requests
from datetime import datetime, timedelta

from django.utils import timezone
from django.db.models import F

from rest_framework import serializers

from v1.constants.constants import BANK_IP

from ..models.transactions import Transaction
from ..models.scan_tracker import ScanTracker
from ..models.treasury import TreasuryStatistic
from ..models.government import GovernmentStatistic
from ..models.statistics import Statistic

from ..utils.parse_memo import parse_memo


def scan_chain(account_number):

    TNBC_TRANSACTION_SCAN_URL = f"http://{BANK_IP}/bank_transactions?account_number={account_number}&block__sender=&fee=&recipient="

    next_url = TNBC_TRANSACTION_SCAN_URL

    if ScanTracker.objects.filter(account_number=account_number).exists():
        scan_tracker = ScanTracker.objects.get(account_number=account_number)
    else:
        error = {"error": "Provided account number does not have entry associated in ScanTracker table!!"}
        raise serializers.ValidationError(error)

    if TreasuryStatistic.objects.filter(account_number=account_number).exists():
        transaction_type = Transaction.TREASURY
    else:
        transaction_type = Transaction.GOVERNMENT

    while next_url:

        try:
            r = requests.get(next_url).json()
        except requests.exceptions.RequestException:
            error = {"error": "Could not scan TNBC chain!!"}
            raise serializers.ValidationError(error)

        next_url = r['next']

        print(next_url)

        for txs in r['results']:

            transaction_time = timezone.make_aware(datetime.strptime(txs['block']['created_date'], '%Y-%m-%dT%H:%M:%S.%fZ'))
            if scan_tracker.last_scanned < transaction_time:

                amount = txs['amount']

                if txs['recipient'] == account_number:
                    direction = Transaction.INCOMING
                else:
                    direction = Transaction.OUTGOING

                if txs['fee'] == "":
                    payment_type = Transaction.NEW
                else:
                    payment_type = Transaction.IS_FEE

                Transaction.objects.create(confirmation_status=Transaction.WAITING_CONFIRMATION,
                                           transaction_type=transaction_type,
                                           direction=direction,
                                           payment_type=payment_type,
                                           sender_account_number=txs['block']['sender'],
                                           recipient_account_number=txs['recipient'],
                                           amount=amount,
                                           block_id=txs['block']['id'],
                                           signature=txs['block']['signature'],
                                           memo=txs['memo'])
            else:
                next_url = None
                break

    scan_tracker.last_scanned = timezone.now()
    scan_tracker.save()
    check_confirmation()
    match_transaction()


def check_confirmation():

    waiting_confirmations_txs = Transaction.objects.filter(confirmation_status=Transaction.WAITING_CONFIRMATION,
                                                           created_at__gt=timezone.now() - timedelta(hours=1))

    for txs in waiting_confirmations_txs:

        r = requests.get(f"http://{BANK_IP}/confirmation_blocks?block={txs.block_id}").json()

        if 'count' in r:
            if int(r['count']) > 0:
                txs.total_confirmations = int(r['count'])
                txs.confirmation_status = Transaction.CONFIRMED

                if txs.transaction_type == Transaction.TREASURY and txs.direction == Transaction.INCOMING:
                    TreasuryStatistic.objects.filter(account_number=txs.recipient_account_number).update(total_tnbc_spent=F('total_tnbc_spent') - txs.amount,
                                                                                                         balance=F('balance') + txs.amount,
                                                                                                         total_transactions=F('total_transactions') + 1,
                                                                                                         last_transaction_amount=txs.amount,
                                                                                                         last_transaction_at=timezone.now())
                elif txs.transaction_type == Transaction.TREASURY and txs.direction == Transaction.OUTGOING:
                    TreasuryStatistic.objects.filter(account_number=txs.sender_account_number).update(total_tnbc_spent=F('total_tnbc_spent') + txs.amount,
                                                                                                      balance=F('balance') - txs.amount,
                                                                                                      total_transactions=F('total_transactions') + 1,
                                                                                                      last_transaction_amount=txs.amount,
                                                                                                      last_transaction_at=timezone.now())

                elif txs.transaction_type == Transaction.GOVERNMENT and txs.direction == Transaction.INCOMING:
                    GovernmentStatistic.objects.all().update(total_tnbc_incoming=F('total_tnbc_incoming') + txs.amount,
                                                             balance=F('balance') + txs.amount,
                                                             total_transactions=F('total_transactions') + 1,
                                                             last_transaction_amount=txs.amount,
                                                             last_transaction_at=timezone.now())
                elif txs.transaction_type == Transaction.GOVERNMENT and txs.direction == Transaction.OUTGOING:
                    GovernmentStatistic.objects.all().update(total_tnbc_spent=F('total_tnbc_spent') + txs.amount,
                                                             balance=F('balance') - txs.amount,
                                                             total_transactions=F('total_transactions') + 1,
                                                             last_transaction_amount=txs.amount,
                                                             last_transaction_at=timezone.now())
                txs.save()


def match_transaction():

    confirmed_new_txs = Transaction.objects.filter(confirmation_status=Transaction.CONFIRMED,
                                                   payment_type=Transaction.NEW)

    for txs in confirmed_new_txs:

        memo_type, github_issue = parse_memo(txs.memo)

        if memo_type == Transaction.TIMESHEET:
            Statistic.objects.all().update(total_paid_to_core_team=F('total_paid_to_core_team') + txs.amount)
        elif memo_type == Transaction.BOUNTY:
            Statistic.objects.all().update(total_paid_as_bounty=F('total_paid_as_bounty') + txs.amount)
        elif memo_type == Transaction.PROJECT:
            Statistic.objects.all().update(total_paid_to_projects=F('total_paid_to_projects') + txs.amount)

        txs.payment_type = memo_type
        txs.github_issue_id = github_issue
        txs.save()
