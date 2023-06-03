from django import forms
from django.contrib.auth.models import User


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
