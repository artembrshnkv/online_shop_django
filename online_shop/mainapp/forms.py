from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

from .models import Comment


class UserRegistrationForm(UserCreationForm):
    # username = forms.CharField(label='fvcd', help_text='ujhbgvf', max_length=255)
    # email = forms.EmailField()
    # password1 = forms.CharField(min_length=8)
    # password2 = forms.CharField(min_length=8)
    # first_name = forms.CharField(max_length=255)
    # last_name = forms.CharField(max_length=255)
    captcha = CaptchaField()


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class AddCommentForm(forms.ModelForm):
    # content = forms.CharField()
    # rating = forms
    # ChoiceField(choices=Comment.stars)
    # product = forms.IntegerField()
    # username = forms.IntegerField()

    class Meta:
        model = Comment
        fields = ['content', 'rating', 'product', 'username']
