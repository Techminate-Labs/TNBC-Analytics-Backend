import uuid

from django.db import models


class ScanTracker(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    account_number = models.CharField(max_length=64, unique=True)
    total_scan = models.IntegerField(default=0)

    last_scanned = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account_number}; Last Run: {self.last_scanned}"
