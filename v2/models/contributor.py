import uuid

from django.db import models

class Contributor(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    tnbc_pk = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    discord = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/team/")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} | {self.role}"

    class Meta:
        verbose_name_plural = "Contributor"
