import uuid

from django.db import models


class GithubIssue(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    issue_id = models.IntegerField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.issue_id} by {self.author}"
