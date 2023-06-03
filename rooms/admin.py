from django.contrib import admin

from .models import Language, Message, Room

admin.site.register(Room)
admin.site.register(Language)
admin.site.register(Message)
