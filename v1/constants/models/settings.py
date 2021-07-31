import uuid

from django.db import models


class Setting(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    reddit_username = models.CharField(max_length=255)
    twitter_username = models.CharField(max_length=255)
    discord_invitation_code = models.CharField(max_length=255)
    github_username = models.CharField(max_length=255)

    def __str__(self):
        return f"Twitter: {self.twitter_username} | GitHub: {self.github_username}"
