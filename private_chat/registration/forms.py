# -*- coding: utf-8 -*-
from django import forms
from .models import UserProfile


class UserForm(forms.ModelForm):
    password_confirmation = forms.CharField(max_length=32, widget=forms.PasswordInput())
    
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'password_confirmation']
        widgets = {'password': forms.PasswordInput()}

    def validate_username(self):
        '''
            проверяем уникальность пользователя
        '''
        username = self.cleanded_data["username"]
        try:
            User.objects.get(username=username)  # тут пытаеися получить юзера
            raise forms.ValidationError("This username has already been created.")  #если получили значит такой есть и делаем исключение
        except:
            return username  #если не найден -- создаем его
		
    def validate_passwords(self): 
        '''  
            проверяем что password == password_confirmation
        '''
        password = self.cleaned_data['password']
        confirm = self.cleaned_data['password_confirmation']
        if password == confirm:
            return password
        else:
            raise forms.ValidationError('password mismath')



class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput())

