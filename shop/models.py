import uuid

from django.db import models


class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=40, default=uuid.uuid4, editable=False)
    userAccount = models.CharField(max_length=20, unique=True)
    mobile = models.CharField(max_length=20, null=True, unique=True)
    email = models.EmailField(unique=True, null=False, default='')
    password = models.CharField(max_length=20, null=False, default='')
    registerTime = models.TimeField(auto_now_add=True, null=True)
    updateTime = models.TimeField(auto_now_add=True, null=True)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return self.userAccount


class GoodType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    registerTime = models.TimeField(auto_now_add=True)
    updateTime = models.TimeField(auto_now_add=True)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return self.name


class Store(models.Model):
    id = models.CharField(auto_created=True, max_length=40, default=uuid.uuid4, editable=False)
    storeId = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Goods(models.Model):
    goodType = models.ForeignKey(GoodType)
    storeId = models.ForeignKey(Store)
    id = models.CharField(auto_created=True, max_length=40, default=uuid.uuid4, editable=False)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goodId = models.BigIntegerField(primary_key=True)
    price = models.FloatField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    fontPageImg = models.CharField(max_length=200, null=False, default='')
    reviews = models.IntegerField(default=0)
    star = models.IntegerField(default=0)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return self.name


class ShoppingCar(models.Model):
    id = models.CharField(primary_key=True, auto_created=True, max_length=40, default=uuid.uuid4, editable=False)
    userId = models.CharField( max_length=40, default=uuid.uuid4, editable=False)
    quantity = models.IntegerField(default=1)
    good = models.ForeignKey('Goods', unique=False)

