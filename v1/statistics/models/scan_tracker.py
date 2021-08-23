import uuid

from django.db import models


class ScanTracker(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    account_number = models.CharField(max_length=64, unique=True)
    last_scanned = models.DateTimeField()

    def __str__(self):
        return f"{self.account_number}; Last Run: {self.last_scanned}"
