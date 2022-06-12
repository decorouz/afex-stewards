import email
from enum import unique
from django.forms import ModelForm

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required")

    class Meta:
        model = User
        fields = ("first_name", "email", "username")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exit")
        return email


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            "first_name",
            "last_name",
            "about",
            "email",
            "username",
            "profile_photo",
            "social_google",
            "social_facebook",
        )
