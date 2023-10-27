from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profil, Skill
from captcha.fields import CaptchaField


class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]
        labels = {
            "first_name": "Ism",
            "last_name": "Familiya",
            "email": "Elektron manzil",
            "username": "Login",
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})


class CustomProfilCreationForm(ModelForm):
    class Meta:
        model = Profil
        fields = [
            "name",
            "email",
            "info",
            "location",
            "bio",
            "social_github",
            "social_youtube",
            "social_facebook",
            "social_linkedin",
            "social_instagram",
            "social_telegram",
            "personal_website",
            "social_leetcode",
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "description"]

        labels = {
            "name": "Malaka nomi",
            "description": "Malakangiz haqida qo'shimcha ma'lumot",  # Correct the field name to match the model
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})
