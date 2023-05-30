from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4



class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # members =
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=400)
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return f'{self.name}'


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]
    

class Language(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name