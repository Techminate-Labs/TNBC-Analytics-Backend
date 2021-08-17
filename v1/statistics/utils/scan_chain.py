import requests
from datetime import datetime, timedelta

from django.utils import timezone

from rest_framework import serializers

from v1.constants.constants import BANK_IP

from ..models.transactions import Transaction
from ..models.scan_tracker import ScanTracker
from ..models.treasury import TreasuryStatistic


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
            r = requests.get(TNBC_TRANSACTION_SCAN_URL).json()
        except requests.exceptions.RequestException:
            error = {"error": "Could not scan TNBC chain!!"}
            raise serializers.ValidationError(error)

        next_url = r['next']

        for txs in r['results']:

            transaction_time = timezone.make_aware(datetime.strptime(txs['block']['created_date'], '%Y-%m-%dT%H:%M:%S.%fZ'))

            if scan_tracker.last_scanned < transaction_time:

                amount = txs['amount']

                if txs['recipient'] == account_number:
                    direction = Transaction.INCOMING
                else:
                    direction = Transaction.OUTGOING

                if txs['fee'] == "":
                    transaction_status = Transaction.NEW
                else:
                    transaction_status = Transaction.IS_FEE

                Transaction.objects.create(confirmation_status=Transaction.WAITING_CONFIRMATION,
                                           transaction_type=transaction_type,
                                           direction=direction,
                                           transaction_status=transaction_status,
                                           sender_account_number=txs['block']['sender'],
                                           recipient_account_number=txs['recipient'],
                                           amount=amount,
                                           block_id=txs['block']['id'],
                                           signature=txs['block']['signature'],
                                           memo=txs['memo'])
            else:
                next_url = None
                break

    scan_tracker.total_scan += 1
    scan_tracker.save()


def check_confirmation():

    waiting_confirmations_txs = Transaction.objects.filter(confirmation_status=Transaction.WAITING_CONFIRMATION,
                                                                 created_at__gt=timezone.now() - timedelta(hours=5))

    for txs in waiting_confirmations_txs:

        r = requests.get(f"http://{BANK_IP}/confirmation_blocks?block={txs.block_id}").json()

        if 'count' in r:
            if int(r['count']) > 0:
                txs.total_confirmations = int(r['count'])
                txs.confirmation_status = Transaction.CONFIRMED
                txs.save()
