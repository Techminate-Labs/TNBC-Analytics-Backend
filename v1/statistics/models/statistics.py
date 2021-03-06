import uuid

from django.db import models


class Statistic(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    total_paid_to_projects = models.IntegerField()
    total_paid_to_core_team = models.IntegerField()
    total_paid_as_bounty = models.IntegerField()

    circulating_supply = models.IntegerField()
    max_supply = models.IntegerField()

    def __str__(self):
        return f"Project: {self.total_paid_to_projects}; CoreTeam: {self.total_paid_to_core_team}; Bounty: {self.total_paid_as_bounty}"
