import uuid

from django.db import models


class GovernmentAccountNumber(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    title = models.CharField(max_length=255)
    account_number = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.title}: {self.account_number}"


class GovernmentStatistic(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    balance = models.IntegerField()
    account_number = models.CharField(max_length=255)
    total_tnbc_incoming = models.IntegerField()
    total_tnbc_spent = models.IntegerField()
    total_transactions = models.IntegerField()
    last_transaction_amount = models.IntegerField()
    last_transaction_at = models.DateTimeField()

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Balance: {self.balance}; Total Spent: {self.total_tnbc_spent}; Last Transaction At: {self.last_transaction_at}"
