import uuid

from django.db import models


class Transaction(models.Model):

    INCOMING = 'INCOMING'
    OUTGOING = 'OUTGOING'

    GOVERNMENT = 'GOVERNMENT'
    TREASURY = 'TREASURY'

    WAITING_CONFIRMATION = 'WAITING_CONFIRMATION'
    CONFIRMED = 'CONFIRMED'

    NEW = 'NEW'
    UNIDENTIFIED = 'UNIDENTIFIED'
    IS_FEE = 'IS_FEE'

    TIMESHEET = 'TIMESHEET'
    PROJECT = 'PROJECT'
    BOUNTY = 'BOUNTY'
    MISCELLANEOUS = 'MISCELLANEOUS'

    transaction_type_choices = [
        (GOVERNMENT, 'Government'),
        (TREASURY, 'Treasury')
    ]

    direction_choices = [
        (INCOMING, 'Incoming'),
        (OUTGOING, 'Outgoing')
    ]

    confirmation_status_choices = [
        (WAITING_CONFIRMATION, 'Waiting Confirmation'),
        (CONFIRMED, 'Confirmed'),
    ]

    payment_type_choices = [
        (NEW, 'New'),
        (TIMESHEET, 'Timesheet'),
        (PROJECT, 'Project'),
        (BOUNTY, 'Bounty'),
        (MISCELLANEOUS, 'Miscellaneous'),
        (UNIDENTIFIED, 'Unidentified'),
        (IS_FEE, 'Is Fee')
    ]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    sender_account_number = models.CharField(max_length=64)
    recipient_account_number = models.CharField(max_length=64)
    github_issue_id = models.IntegerField(default=0)
    amount = models.IntegerField()
    memo = models.CharField(max_length=255, null=True, blank=True)
    signature = models.CharField(max_length=255)
    block_id = models.CharField(max_length=255)

    transaction_type = models.CharField(max_length=255, choices=transaction_type_choices)
    direction = models.CharField(max_length=255, choices=direction_choices)
    confirmation_status = models.CharField(max_length=255, choices=confirmation_status_choices)
    payment_type = models.CharField(max_length=255, choices=payment_type_choices)
    txs_sent_at = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Direction: {self.direction}; Amount: {self.amount}; {self.confirmation_status}"
