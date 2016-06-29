# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User 
from django.core.validators import RegexValidator
from .models import UserProfile


class UserForm(forms.ModelForm):
    password_confirmation = forms.CharField(max_length=32, widget=forms.PasswordInput())
    
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'password_confirmation']
        widgets = {'password': forms.PasswordInput()}

    def clean(self): # сдесь происходит валидация пароля
        cleaned_data = super(UserForm, self).clean()                     # переопреледением метода clean() 
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('password_confirmation')
        if password != confirm:                                             # и при несовпадении
            raise forms.ValidationError({'password': 'Passwords mismatch'}) # бросаем исключение


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput())

