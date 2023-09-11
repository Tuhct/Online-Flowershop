from django.contrib import admin
from article.models import User,Article
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """创建UserAdmin，类，继承于admin，article"""
    #配置展示列表，在User板块下的列表展示
    list_display = ('username','email')
    #配置过滤查询字段，在USer板块下的右侧过滤框
    list_filter = ('username','email')
    #配置可以搜索的字段，在User板块下的右搜索框
    search_fields = (['username','email'])

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','publish_date')
    list_filter = ('title',)
    search_fields = ('title',)

#admin.site.register(User,UserAdmin)
#admin.site.register(Article,ArticleAdmin)