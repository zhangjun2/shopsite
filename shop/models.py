from django.db import models


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(auto_created=True)
    storeId = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Goods(models.Model):
    goodType = models.ForeignKey(GoodType)
    storeId = models.ForeignKey(Store)
    id = models.IntegerField(auto_created=True)
    goodId = models.BigIntegerField(primary_key=True)
    price = models.FloatField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    fontPageImg = models.CharField(max_length=200, null=False, default='')

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return self.name


class ShoppingCar(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    quantity = models.IntegerField(default=1)
    good = models.ForeignKey('Goods', unique=False)

