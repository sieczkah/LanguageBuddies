from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserForm(forms.ModelForm):
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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio_field", "personal_web", "avatar")
        widgets = {
            "bio_field": forms.TextInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "id": "floatingBioField",
                }
            ),
            "personal_web": forms.TextInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "placeholder": "Personal link",
                }
            ),
            "avatar": forms.TextInput(
                attrs={"class": "form-control", "id": "floatingAvatar"}
            ),
        }
