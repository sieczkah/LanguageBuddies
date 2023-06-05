from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(User, related_name="members", blank=True)
    language = models.ForeignKey("Language", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=400)
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self) -> str:
        return f"{self.name}"


class Message(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    # To update the "updated" field everytime the message is sent
    # The save method of models.model is overriden
    def save(self, *args, **kwargs):
        self.room.updated = timezone.now()
        self.room.save()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-sent"]

    def __str__(self):
        return self.body[:50]


class Language(models.Model):
    name = models.CharField(max_length=250)
    alpha_2 = models.CharField(max_length=2, default="PL")

    def __str__(self):
        return self.name
