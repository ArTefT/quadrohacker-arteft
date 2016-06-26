from django import forms
from .models import UserProfile


class UserForm(forms.ModelForm):
    password_confirmation = forms.CharField(max_length=32, widget=forms.PasswordInput())
    
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'password_confirmation']
        widgets = {'password': forms.PasswordInput()}


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput())
