from django.db import models


# Create your models here.
class User(models.Model):
    """User模型类，数据类型应该继承于models.Model或其子类"""
    id=models.IntegerField(primary_key=True)#主键
    username=models.CharField(max_length=30)#用户名，字符串类型
    email=models.CharField(max_length=30)#邮箱，字符串类型


class Article(models.Model):
    """Article模型类，数据类型应该继承于model.Model或其子类"""
    id=models.IntegerField(primary_key=True)#主键
    title=models.CharField(max_length=120)#标题，字符串类型
    content=models.TextField()#内容，文本类型
    publish_date=models.DateTimeField()#出版日期，日期时间类型
    user=models.ForeignKey(User,on_delete=models.CASCADE)#设置外键