# -*- coding:utf-8 -*-
from django import forms

class SendMessageForm(forms.Form):
    text_message = forms.CharField()

