import uuid

from django.db import models

class Profile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    facebook = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    reddit = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    discord = models.CharField(max_length=255)
    github = models.CharField(max_length=255)

    def __str__(self):
        return f"Facebook: {self.facebook} | GitHub: {self.github}"

    class Meta:
        verbose_name_plural = "Profile"