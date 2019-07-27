from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import ProfileModel
from django.forms import ValidationError


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Please provide a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()

        try:
            email = cleaned_data['email']
        except KeyError:
            raise ValidationError("")

        if email and User.objects.filter(email=email).count() > 0:
            raise ValidationError(u"Email already exists.")

        return cleaned_data


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Please provide a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['university', 'bio', 'profile_image']
