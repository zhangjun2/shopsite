import uuid
from sqlite3 import Date

from django.db import models
from django.utils.timezone import now


class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=40, default=uuid.uuid4, editable=False)
    userAccount = models.CharField(max_length=20, unique=True)
    mobile = models.CharField(max_length=20, null=True, unique=True)
    email = models.EmailField(unique=True, null=False, default='')
    password = models.CharField(max_length=20, null=False, default='')
    registerTime = models.TimeField(auto_now_add=True, null=True)
    updateTime = models.TimeField(auto_now_add=True, null=True)

    def __repr__(self):
        return self.userAccount

    def __str__(self):
        return self.userAccount

    class Meta():
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class GoodType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    creatTime = models.TimeField(auto_now_add=True, null=True)
    updateTime = models.TimeField(auto_now_add=True, null=True)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return self.name


class Store(models.Model):
    id = models.CharField(primary_key=True, auto_created=True, max_length=40, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)


class Goods(models.Model):
    good_id = models.CharField(primary_key=True, auto_created=True, max_length=40, default=uuid.uuid4, editable=False)
    goodType = models.ForeignKey(GoodType)
    price = models.FloatField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    fontPageImg = models.ImageField(upload_to='fontPageImg')
    reviews = models.IntegerField(default=0)
    star = models.IntegerField(default=0)
    creatTime = models.TimeField(auto_now_add=True, null=True)
    updateTime = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    __repr__ = __str__

    class Meta():
        verbose_name = '商品'
        verbose_name_plural = verbose_name


class ShoppingCar(models.Model):
    id = models.CharField(primary_key=True, auto_created=True, max_length=40, default=uuid.uuid4, editable=False)
    userId = models.CharField( max_length=40, default=uuid.uuid4, editable=False)
    quantity = models.IntegerField(default=1)
    good = models.ForeignKey('Goods', unique=False)
    creatTime = models.TimeField(auto_now_add=True, null=True)
    updateTime = models.TimeField(auto_now_add=True, null=True)


class Manager(models.Model):
    manage_id = models.CharField(primary_key=True, auto_created=True, max_length=40, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20, unique=False)
    userAccount = models.CharField(max_length=20, unique=True)
    mobile = models.CharField(max_length=20, null=True, unique=True)
    email = models.EmailField(unique=True, null=False, default='')
    password = models.CharField(max_length=20, null=False, default='')
    registerTime = models.TimeField(auto_now_add=True, null=True)
    updateTime = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username

    class Meta():
        verbose_name = '管理员'
        verbose_name_plural = verbose_name

