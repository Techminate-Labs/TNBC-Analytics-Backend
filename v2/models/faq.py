import uuid
from django.db import models

class FaqType(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "FAQ Categories"

class Faq(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    faqType_id = models.ForeignKey(FaqType, on_delete=models.DO_NOTHING)
    question = models.TextField()
    answer = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "FAQs"
