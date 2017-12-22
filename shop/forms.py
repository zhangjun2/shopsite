#-*- coding:utf-8 -*-
from django import forms

from shop.models import GoodType

_author__ = 'ZHANGJUN'


class RegisterForm(forms.Form):
    email = forms.EmailField()
    account = forms.CharField()
    password = forms.CharField()


class GoodForm(forms.Form):
    # good_id = forms.CharField(primary_key=True, auto_created=True, max_length=40)
    # goodType = forms.ForeignKey(GoodType)
    price = forms.FloatField(label='价格')
    name = forms.CharField(label='名称', max_length=100)
    description = forms.CharField(label='描述', max_length=200)
    # fontPageImg = forms.FileField(label='缩略图')

