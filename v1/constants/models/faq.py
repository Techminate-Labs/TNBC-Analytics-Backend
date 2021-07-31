import uuid
from django.db import models


class FaqCategory(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    category = models.ForeignKey(FaqCategory, on_delete=models.DO_NOTHING)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
