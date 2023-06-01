from django import forms

from .models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ("language", "name", "description")

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "language": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }


class RoomEditForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["name", "description"]
