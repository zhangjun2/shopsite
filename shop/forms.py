#-*- coding:utf-8 -*-
from django import forms

_author__ = 'ZHANGJUN'


class RegisterForm(forms.Form):
    email = forms.EmailField()
    account = forms.CharField()
    password = forms.CharField()