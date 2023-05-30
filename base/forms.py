from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class RoomEditForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description']