#-*- coding:utf-8 -*-
from shop.models import ShoppingCar

_author__ = 'ZHANGJUN'

# count = ShoppingCar.objects.filter(good__name='Nike LBJII').values('id')
# print(count)

a,b,n = 0,1,0;
while(n<20):
	print(b)
	a=b
	b = a+b
	n = n+1
