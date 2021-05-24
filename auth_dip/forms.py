from .models import AuthDb
from django.forms import ModelForm, TextInput, PasswordInput
from django.utils.translation import ugettext_lazy as _


class AuthDbForm(ModelForm):
    class Meta:
        model = AuthDb
        fields = ['Login', 'Password']

        widgets = {
            "Login": TextInput(attrs={

                "class": "form-control",
                "placeholder": "Enter username"
            }),
            "Password": PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Enter password"
            })
        }

        labels = {
            "Login": _("User"),
            "Password": _("Password")
        }