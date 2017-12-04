import json

from django.core import serializers
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, StreamingHttpResponse
from django.shortcuts import render, redirect

# Create your view here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from shop import cartApi
from shop.models import Customer, Goods, ShoppingCar, Manager


def index(request, ismanager=False):
    regsite_manager()
    if ismanager:
        return render(request, 'home_m.html')
    else:
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
        # for good in goods:
        #     good.good_id = str(good.good_id)
        return render(request, 'index.html', {'goods': list(goods)})


def detail(request, id):
    # good_id = int(id)
    if id:
        good = Goods.objects.filter(good_id=id).first()
        good.reviews += 1
        good.save()
        return render(request, 'details.html', {'good': good})


# 加入购物车
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


# 管理员添加产品
@csrf_exempt
def addgood(req):
    if req.method == 'POST':
        good = Goods.objects.create(
            name=req.POST['name'],
            price=req.POST['price'],
            description=req.POST['description'],
            fontPageImg=req.FILES.get('fontimage'),
            goodType_id=req.POST['type']
        )
        if good:
            return HttpResponse('添加成功')
        else:
            return HttpResponse('添加失败!')
    pass


# 注册一个管理员账号
def regsite_manager():
    if Manager.objects.first():
        pass
    else:
        manager = Manager.objects.create(username='张军',userAccount='zhangjun',password='zhangjun6615');
        manager.save()