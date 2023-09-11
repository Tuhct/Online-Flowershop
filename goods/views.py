from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from goods.models import flowersCategory, flowerInfo
from django.shortcuts import render

def index(request):
    categories = flowersCategory.objects.all()
    for cag in categories:
        # cag.flowerinfo_set.all()
        # flowerInfo.objects.filter()
        cag.flower_list = cag.flowerinfo_set.order_by('-id')[:4]

        # 购物车cookie
        cart_flower_list = []
        cart_flower_count = 0
        for flower_id, flower_num in request.COOKIES.items():
            if not flower_id.isdigit():
                # return
                continue
            cart_flowers = flowerInfo.objects.get(id=flower_id)
            cart_flowers.flower_num = flower_num
            cart_flower_list.append(cart_flowers)
            cart_flower_count = cart_flower_count + int(flower_num)
    return render(request, 'index.html', {'categories': categories,
                                          'cart_flower_list': cart_flower_list,
                                          'cart_flower_count': cart_flower_count})


def detail(request):
    categories = flowersCategory.objects.all()
    cart_flower_list = []
    cart_flower_count = 0
    for flower_id, flower_num in request.COOKIES.items():
        if not flower_id.isdigit():
            # return
            continue
        cart_flowers = flowerInfo.objects.get(id=flower_id)
        cart_flowers.flower_num = flower_num
        cart_flower_list.append(cart_flowers)
        cart_flower_count = cart_flower_count + int(flower_num)

    flower_id = request.GET.get('id', 1)
    flower_data = flowerInfo.objects.get(id=flower_id)

    return render(request, 'detail.html', {'categories': categories,
                                           'cart_flower_list': cart_flower_list,
                                           'cart_flower_count': cart_flower_count,
                                           'flower_data': flower_data})


def flower(request):
    categories = flowersCategory.objects.all()
    cag_id = request.GET.get('cag', 1)
    page_id = request.GET.get('page', 1)
    # 获取当前的分类 对象
    current_cag = flowersCategory.objects.get(id=cag_id)
    # current_cag.goodsinfo set.all()
    # GoodsInfo.objects.filter(goods_cag=current_cag)
    # #当前分类下的所有商品
    flower_data = flowerInfo.objects.filter(flower_cag_id=cag_id)
    paginator = Paginator(flower_data, 12)
    page_data = paginator.page(page_id)
    # 所有分类

    # 购物车所有商品
    cart_flower_list = []  # 购物车总数量
    cart_flower_count = 0
    for flower_id, flower_num in request.COOKIES.items():
        if not flower_id.isdigit():
            continue
        cart_flowers = flowerInfo.objects.get(id=flower_id)
        cart_flowers.flower_num = flower_num
        cart_flower_list.append(cart_flowers)
        cart_flower_count = cart_flower_count + int(flower_num)

    return render(request, 'flower.html', {'current_cag': current_cag,
                                           'page_data': page_data,
                                           'flower_data': flower_data,
                                           'cart_flower_list': cart_flower_list,
                                           'categories': categories,
                                           'cart_flower_count': cart_flower_count,
                                           'paginator': paginator,
                                           'cag_id': cag_id})
