#-*- coding:utf-8 -*-
_author__ = 'ZHANGJUN'

from django.core import serializers
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, StreamingHttpResponse
from django.shortcuts import render, redirect

# Create your view here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from shop import cartApi
from shop.models import Customer, Goods, ShoppingCar

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        c = Customer.objects.filter(email=email, password=password).first()
        if c:
            request.session['username'] = c.userAccount
            request.session['userId'] = c.id
            return redirect(reverse('index'))
        else:
            return HttpResponse('邮箱或者密码错误！')
    else:
        return render(request, 'login.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        p = Customer.objects.filter(email=email)
        if len(p) > 0:
            return HttpResponse('邮箱已被注册')
        else:
            user = Customer.objects.create(userAccount=username, email=email, password=password)
            if user:
                request.session['username'] = user.userAccount
                request.session['userId'] = str(user.id)
            return redirect(reverse('index'))
    else:
        return render(request, 'register.html')
