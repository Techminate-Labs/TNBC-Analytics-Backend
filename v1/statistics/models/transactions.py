import uuid

from django.db import models

from .github import GithubIssue


class Transaction(models.Model):

    INCOMING = 'INCOMING'
    OUTGOING = 'OUTGOING'

    GOVERNMENT = 'GOVERNMENT'
    TREASURY = 'TREASURY'

    WAITING_CONFIRMATION = 'WAITING_CONFIRMATION'
    CONFIRMED = 'CONFIRMED'

    NEW = 'NEW'
    IDENTIFIED = 'IDENTIFIED'
    UNIDENTIFIED = 'UNIDENTIFIED'
    IS_FEE = 'IS_FEE'

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

    transaction_status_choices = [
        (NEW, 'New'),
        (IDENTIFIED, 'Identified'),
        (UNIDENTIFIED, 'Unidentified'),
        (IS_FEE, 'Is Fee')
    ]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    sender_account_number = models.CharField(max_length=64)
    recipient_account_number = models.CharField(max_length=64)
    github_issue = models.ForeignKey(GithubIssue, on_delete=models.DO_NOTHING, null=True, blank=True)
    amount = models.IntegerField()
    memo = models.CharField(max_length=255, null=True, blank=True)
    signature = models.CharField(max_length=255)
    block_id = models.CharField(max_length=255)

    transaction_type = models.CharField(max_length=255, choices=transaction_type_choices)
    direction = models.CharField(max_length=255, choices=direction_choices)
    confirmation_status = models.CharField(max_length=255, choices=confirmation_status_choices)
    transaction_status = models.CharField(max_length=255, choices=transaction_status_choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Direction: {self.direction}; Amount: {self.amount}; {self.confirmation_status}"
