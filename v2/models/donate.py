import uuid

from django.db import models


class Donate(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    logo = models.ImageField(upload_to="images/qr/")
    public_key = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.public_key}"

    class Meta:
        verbose_name_plural = "Donate"
