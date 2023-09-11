from django.db import models

# Create your models here.

#花分类表
#模型类 对应一张表
class flowersCategory(models.Model):
    # 分类的名称
    cag_name=models.CharField(max_length=30)
    # 分类的样式
    cag_css=models.CharField(max_length=200)
    # 分类的图片
    cag_img=models.ImageField(upload_to='cag')

# 花表
class flowerInfo(models.Model):
    #花名
    flower_name=models.CharField(max_length=100,verbose_name='商品名')
    #花价格
    flower_price=models.IntegerField(default=0,verbose_name='价格')
    #花语
    flower_desc=models.CharField(max_length=2000,verbose_name='介绍')
    #花图
    flower_img=models.ImageField(upload_to='flower',verbose_name='图像')
    #所属分类
    flower_cag=models.ForeignKey('flowersCategory',on_delete=models.CASCADE)

    def __str__(self):
        return self.flower_name