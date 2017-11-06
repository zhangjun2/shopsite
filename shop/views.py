import json

from django.core import serializers
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, StreamingHttpResponse
from django.shortcuts import render, redirect

# Create your view here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from shop import cartApi
from shop.models import Customer, Goods, ShoppingCar


def index(request):
    page = request.GET.get('page')
    if page is None:
        goods = Goods.objects.all()[0:10]
        # goods1 = Goods.objects.values('name', 'price')
        # goods2 = Goods.objects.values_list('name')
    else:
        goods = Goods.objects.all()[(int(page)-1)*10:int(page)*10]
    # print(goods1)
    # print(goods2)

    # count  = ShoppingCar.objects.values('good_id').annotate(count=Count('id'))
    # count = ShoppingCar.objects.filter(good__name='Nike LBJII').values('id')
    # print(count)
    print(list(goods))
    return render(request, 'index.html', {'goods': list(goods)})


def detail(request, id):
    good_id = int(id)
    if good_id:
        good = Goods.objects.filter(goodId=good_id).first()
        good.reviews += 1
        good.save()
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
                request.session['userId'] = str(user.id)
            return redirect(reverse('index'))
    else:
        return render(request, 'register.html')


#加入购物车
def addcar(req):
    goodId = req.GET.get('goodId')
    quantity = req.GET.get('quantity')
    good = Goods.objects.filter(goodId=goodId).first()
    print(good)
    print(quantity)
    userId = req.session['userId']
    car = ShoppingCar.objects.create(userId=userId, quantity=quantity, good=good)
    if car:
        return HttpResponse('河涸海干', content_type='application/json')


@csrf_exempt
def download(req):
    the_file_name = 'jenkins.war'  # 显示在弹出对话框中的默认的下载文件名
    filename = 'D:\soft\下载\jenkins.war'  # 要下载的文件路径
    response = StreamingHttpResponse(readFile(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response


def readFile(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


# 查询购物车商品总数
def queryCar(req):
    userId = req.session['userId']
    response_data = {}
    response_data['count'] = cartApi.getCartCount(userId)
    response_data['goods'] = serializers.serialize('json', cartApi.getCartGoods(userId))
    return HttpResponse(json.dumps(response_data), content_type="application/json")


# 查看购物车的商品
def cartView(req):
    userId = req.session['userId']
    s = cartApi.getCartGoods(userId)
    print(s)
    return render(req, 'cart.html', {'goods': s})


