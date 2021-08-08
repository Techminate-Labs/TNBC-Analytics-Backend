import uuid

from django.db import models

from .github import GithubIssue


class GovernmentTransaction(models.Model):

    INCOMING = 'INCOMING'
    OUTGOING = 'OUTGOING'

    direction_choices = [
        (INCOMING, 'Incoming'),
        (OUTGOING, 'Outgoing')
    ]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    sender_account_number = models.CharField(max_length=64)
    recipient_account_number = models.CharField(max_length=64)
    github_issue = models.ForeignKey(GithubIssue, on_delete=models.DO_NOTHING)
    direction = models.CharField(max_length=255, choices=direction_choices)
    amount = models.IntegerField()
    fee = models.IntegerField()
    memo = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Direction: {self.direction}; Amount: {self.amount}"


class TreasuryTransaction(models.Model):

    INCOMING = 'INCOMING'
    OUTGOING = 'OUTGOING'

    direction_choices = [
        (INCOMING, 'Incoming'),
        (OUTGOING, 'Outgoing')
    ]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    sender_account_number = models.CharField(max_length=64)
    recipient_account_number = models.CharField(max_length=64)
    github_issue = models.ForeignKey(GithubIssue, on_delete=models.DO_NOTHING)
    direction = models.CharField(max_length=255, choices=direction_choices)
    amount = models.IntegerField()
    fee = models.IntegerField()
    memo = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Direction: {self.direction}; Amount: {self.amount}"
