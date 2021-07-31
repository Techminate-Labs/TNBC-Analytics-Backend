import uuid

from django.db import models


class Team(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    name = models.CharField(max_length=255)
    github_username = models.CharField(max_length=255)
    discord_username = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    image = models.URLField()

    def __str__(self):
        return f"{self.name} | {self.role} | {self.account_number}"
