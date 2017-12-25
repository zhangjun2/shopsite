import json

from django.core import serializers
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import render, redirect

# Create your view here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from shop import cartApi
from shop.forms import GoodForm
from shop.models import Customer, Goods, ShoppingCar, Manager
from shop.util.jsonresponse import JsonResponse


def index(request, ismanager=False):
    regsite_manager()
    page = request.GET.get('page')
    if page is None:
        goods = Goods.objects.all()[0:10]
        # goods1 = Goods.objects.values('name', 'price')
        # goods2 = Goods.objects.values_list('name')
    else:
        goods = Goods.objects.all()[(int(page)-1)*10:int(page)*10]
    if request.session.get('ismanager'):
        return render(request, 'good_list_m.html', {'goods': goods})
    else:
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
    good = Goods.objects.filter(good_id=goodId).first()
    print(good)
    print(quantity)
    userId = req.session['userId']
    car_good = ShoppingCar.objects.filter(userId=userId, good=good).first()
    if car_good:
        count = int(quantity)+int(car_good.quantity)
        car_good.quantity = count
        car_good.save()
    else:
        car = ShoppingCar.objects.create(userId=userId, quantity=quantity, good=good)
    res = JsonResponse()
    res.status = res.STATUS_SUCCESS
    return HttpResponse(json.dumps(res, default=lambda obj: obj.__dict__), content_type="application/json")


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
    userId = req.session.get('userId')
    if userId:
        response_data = {}
        response_data['count'] = cartApi.getCartCount(userId)
        response_data['goods'] = serializers.serialize('json', cartApi.getCartGoods(userId))
        res = JsonResponse()
        res.status = res.STATUS_SUCCESS
        res.data = response_data
        # print(res)
        # response_data['res'] = json.dumps(res)
        return HttpResponse(json.dumps(res, default=lambda obj: obj.__dict__), content_type="application/json")


# 查看购物车的商品
def cartView(req):
    userId = req.session['userId']
    s = cartApi.getCartGoods(userId)
    print(s)
    return render(req, 'cart.html', {'goods': s})


# 管理员添加产品
# @csrf_exempt
def addgood(req):
    if req.method == 'POST':
        good_form = GoodForm(req.POST, req.FILES)
        if good_form.is_valid():
            # good = Goods.objects.create(
            #     name=req.POST['name'],
            #     price=req.POST['price'],
            #     description=req.POST['description'],
            #     fontPageImg=req.FILES.get('fontimage'),
            #     goodType_id=req.POST['type']
            # )
            good = Goods.objects.create(
                name=good_form.cleaned_data['name'],
                price=good_form.cleaned_data['price'],
                description=good_form.cleaned_data['description'],
                fontPageImg=good_form.cleaned_data['fontPageImg'],
                goodType_id=1
            )
            if good:
                return redirect(reverse('index'))
            else:
                return HttpResponse('添加失败!')
        else:
            return HttpResponse('添加失败!')
    else:
        form = GoodForm()
        return render(req, 'add_good_m.html', {'form': form})


def editgood(request):
    page = request.GET.get('page')
    if page is None:
        goods = Goods.objects.all()[0:10]
        # goods1 = Goods.objects.values('name', 'price')
        # goods2 = Goods.objects.values_list('name')
    else:
        goods = Goods.objects.all()[(int(page) - 1) * 10:int(page) * 10]
    return render(request, 'good_list_m.html', {'goods': goods})


def deletegood(request):
    good_id = request.GET.get('id')
    Goods.objects.filter(good_id=good_id).delete()
    response_data = {}
    response_data['status'] = 'SUCCESS'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


# 注册一个管理员账号
def regsite_manager():
    if Manager.objects.first():
        pass
    else:
        manager = Manager.objects.create(username='张军',userAccount='zhangjun',password='zhangjun6615')