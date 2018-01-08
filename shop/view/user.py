# -*- coding:utf-8 -*-
import json

from django.contrib.sessions.backends.db import SessionStore

from shop.util.jsonresponse import JsonResponse

_author__ = 'ZHANGJUN'

from django.core import serializers
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import render, redirect

# Create your view here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from shop import cartApi
from shop.models import Customer, Goods, ShoppingCar, Manager


@csrf_exempt
def login(request):
	if request.method == 'POST':
		ismanager = request.POST.get('ismanager')
		print(ismanager)
		if ismanager:
			request.session['ismanager'] = True
			userAccount = request.POST['email']
			password = request.POST['password']
			c = Manager.objects.filter(userAccount=userAccount, password=password).first()
			if c:
				request.session['username'] = c.userAccount
				request.session['userId'] = c.manage_id
				request.session['islogin'] = True
				# return redirect(reverse('index'))
				res = JsonResponse()
				res.status = JsonResponse.STATUS_SUCCESS
				res.data = {"userid": c.manage_id}
				return HttpResponse(json.dumps(res, default=lambda obj: obj.__dict__), content_type="application/json")
			else:
				# return HttpResponse('管理员登录失败')
				res = JsonResponse()
				res.status = JsonResponse.STATUS_ERROR
				res.errorMsg = "管理员登录失败"
				return HttpResponse(json.dumps(res, default=lambda obj: obj.__dict__), content_type="application/json")
		else:
			request.session['ismanager'] = False
			email = request.POST['email']
			password = request.POST['password']
			c = Customer.objects.filter(email=email, password=password).first()
			if c:
				request.session['username'] = c.userAccount
				request.session['userId'] = c.id
				request.session['islogin'] = True
				# return redirect(reverse('index'))
				res = JsonResponse()
				res.status = JsonResponse.STATUS_SUCCESS
				res.data = {"userid": c.id}
				return HttpResponse(json.dumps(res, default=lambda obj: obj.__dict__), content_type="application/json")
			else:
				res = JsonResponse()
				res.status = JsonResponse.STATUS_ERROR
				res.errorMsg = "登录失败"
				return HttpResponse(json.dumps(res, default=lambda obj: obj.__dict__), content_type="application/json")
				# return HttpResponse('邮箱或者密码错误！')
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
				request.sesson['islogin'] = True
			return redirect(reverse('index'))
	else:
		return render(request, 'register.html')


def logout(req):
	if req.method == 'GET':
		print(type(req.session))
		if req.session.get('userId'):
			del req.session['userId']
			del req.session['username']
			del req.session['islogin']
		return redirect(reverse('login'))
