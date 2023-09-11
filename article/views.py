from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from article.models import Article, User
from django.views import View
from article.forms import LoginForm

from django.contrib.auth.models import Group
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {"articles": articles})
    # return HttpResponse('article_list函数')


def year_archive(request, year):
    return HttpResponse(f'year_archive 函数接受参数：{year}')


def month_archive(request, year, month):
    return HttpResponse(f'month_archive 函数接受参数year:{year},month:{month}')


def article_detail(request, year, month, slug):
    return HttpResponse(f'month_archive 函数接受参数year:{year},month:{month},slug:{slug}')


def article_re(request, year):
    return HttpResponse(f'year 正则表达式：{year}')


def get_current_datetime(request):  # 定义一个视图方法，必须带有请求对象作为参数
    today = datetime.today()  # 请求时间
    formatted_today = today.strftime('%y-%m-%d')
    html = f"<html><body>今天是{formatted_today}</body></html>"  # 生成html代码
    return HttpResponse(html)  # 将相应对象返回，数据为生成的HTML代码


class LoginFormView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'form': LoginForm()})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            return HttpResponse(f'用户名:{username},邮箱:{email}')
        else:
            return render(request, 'login.html', {'form': form})
    #group = Group.objects.get(id=1)
    #User.groups.add(group)
