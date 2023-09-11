import datetime

import django
from django.db import models
import django.utils.timezone


# Create your models here.

class OrderInfo(models.Model):
    status=(
        (1,'待付款'),
        (2,'待发货'),
        (3, '待收货'),
        (4, '已完成'),
    )
    # 订单编号
    order_id=models.CharField(max_length=100)
    # 收货地址
    order_addr=models.CharField(max_length=100)
    # 收货人
    order_recv=models.CharField(max_length=50)
    # 联系电话
    order_tele=models.CharField(max_length=11)
    # 运费
    order_fee=models.IntegerField(default=0)
    # 订单状态
    order_status=models.IntegerField(default=1,choices=status)
    # 送达时间
    order_time=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.order_id

class OrderFlowers(models.Model):
    # 所属商品
    flower_info= models.ForeignKey('goods.flowerInfo',on_delete=models.CASCADE)
    # 花数量
    flower_num=models.IntegerField()
    # 订单信息
    flower_order=models.ForeignKey('OrderInfo',on_delete=models.CASCADE)

class User(models.Model):
    """User模型类，数据类型应该继承于models.Model或其子类"""
    id=models.IntegerField(primary_key=True)#主键
    username=models.CharField(max_length=30)#用户名，字符串类型
    email=models.CharField(max_length=30)#邮箱，字符串类型