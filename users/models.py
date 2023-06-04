from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models

from helpers import avatar_maker

avatar_svg = avatar_maker.create_avatar()


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio_field = models.CharField(max_length=250, blank=True, null=True)
    avatar = models.TextField(default=avatar_svg, blank=True, null=True)
    personal_web = models.CharField(max_length=1000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return f"{self.user.username}"
