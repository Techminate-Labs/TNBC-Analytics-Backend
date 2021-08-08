import uuid

from django.db import models


class TreasuryStatistic(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    account_number = models.CharField(max_length=64)
    balance = models.IntegerField()
    total_tnbc_spent = models.IntegerField()
    total_transactions = models.IntegerField()
    last_transaction_amount = models.IntegerField()
    last_transaction_at = models.DateTimeField()

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Balance: {self.balance}; Total Spent: {self.total_tnbc_spent}; Last Transaction At: {self.last_transaction_at}"
