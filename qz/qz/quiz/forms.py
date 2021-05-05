from django import forms
from quiz.models import UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text=False)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):

     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site', 'profile_pic')
