from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    # username = forms.CharField(label='fvcd', help_text='ujhbgvf', max_length=255)
    # email = forms.EmailField()
    # password1 = forms.CharField(min_length=8)
    # password2 = forms.CharField(min_length=8)
    # first_name = forms.CharField(max_length=255)
    # last_name = forms.CharField(max_length=255)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
