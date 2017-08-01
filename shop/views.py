import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from shop.models import Customer, Goods


def index(request):
    page = request.GET.get('page')
    if page is None:
        goods = Goods.objects.all()[0:10]
    else:
        goods = Goods.objects.all()[(int(page)-1)*10:int(page)*10]
    print(goods)
    return render(request, 'index.html', {'goods': goods})


def detail(request, id):
    good_id = int(id)
    if good_id:
        good = Goods.objects.filter(goodId=good_id)
        return render(request, 'details.html', {'good': good})


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
                request.session['userId'] = user.id
            return redirect(reverse('index'))
    else:
        return render(request, 'register.html')


def addcar(req):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)