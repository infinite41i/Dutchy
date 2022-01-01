from django import forms
from django.contrib.auth.models import User

from account.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)
    name = forms.CharField(required=True)

    def save(self, *args, **kwargs):
        user = User(first_name=self.cleaned_data["name"],
                    username=self.cleaned_data["username"]
                    )
        user.set_password(self.cleaned_data["password"])
        user.save()
        profile = Profile(user=user)
        profile.save()
