#-*- coding:utf-8 -*-
import json

from django.core import serializers
from django.http import HttpResponse

from shop.models import ShoppingCar

_author__ = 'ZHANGJUN'


def getCartCount(userId):
    goodsId = ShoppingCar.objects.filter(userId=userId).all()
    count = goodsId.count()
    # response_data = {}
    # response_data['count'] = count
    # response_data['goods'] = serializers.serialize("json", goods)
    return count


def getCartGoods(userId):
    goods = ShoppingCar.objects.filter(userId=userId).all()
    return goods