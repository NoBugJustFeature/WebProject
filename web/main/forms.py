from django import forms
from .models import Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email']

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comments
        fields = ["comment"]
        widgets = {"comment": forms.Textarea(attrs={
            "placeholder": "Оставьте свой отзыв",
            'class': "textarea-style",
            })
        }
