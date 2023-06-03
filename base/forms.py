from django import forms
from django.contrib.auth.models import User

from .models import Room


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "id": "floatingFirstName"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "id": "floatingLastName"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control", "id": "floatingEmail"}
            ),
        }


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

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }
