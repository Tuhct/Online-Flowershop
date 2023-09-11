import time
from cart.models import OrderInfo, OrderFlowers
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from goods.models import flowerInfo
# views.py
'''from django.contrib.auth.decorators import login_required
# 在类之前需要添加以下两行代码
from django.utils.decorators import method_decorator
@method_decorator(login_required,name='dispatch')
class LoginView(View):
    def get(self,request):
        pass
    def post(self,request):
    	pass'''


# Create your views here.

def add_cart(request):
    """深加到购物车 cookie goods id:count"# 1获取传过来的商品的id"""
    flower_id = request.GET.get('id', '')
    if flower_id:
        # 获取上一个页面的地址
        prev_url = request.META['HTTP_REFERER']
        print(prev_url)
        response = redirect(prev_url)
        # 2把商品id存到cookie里
        # 获职之前商品在购物车的故量
        flower_count = request.COOKIES.get(flower_id)  # 如果之前购物车里有商品 那么就在之前的数量上+1#如果之前没有 那么就添加1个
        if flower_count:
            flower_count = int(flower_count) + 1
        else:
            flower_count = 1
        response.set_cookie(flower_id, flower_count)
    return response
    # Create your views here.


def show_cart(request):
    # 1获职购物车商品列表
    cart_flower_list = []
    # 2购物车商品的总效量
    cart_flower_count = 0
    # 3购物车的总价格
    cart_flower_money = 0

    # 从cookie获职数据 遍历cookie goods_id:count
    for flower_id, flower_num in request.COOKIES.items():
        # 判断id是不是数字 来确定是不是商品数据
        if not flower_id.isdigit():
            continue
        # 根据id获取商品对象

        cart_flowers = flowerInfo.objects.get(id=flower_id)
        # 并把商品量    存到对应的对象里
        cart_flowers.flower_num = flower_num
        cart_flowers.total_money = int(flower_num) * cart_flowers.flower_price
        cart_flower_list.append(cart_flowers)
        cart_flower_count += int(flower_num)
        cart_flower_money += int(flower_num) * cart_flowers.flower_price

    return render(request, 'cart.html', {'cart_flower_list': cart_flower_list,
                                         'cart_flower_count': cart_flower_count,
                                         'cart_flower_money': cart_flower_money,
                                         })


def remove_cart(request):
    flower_id = request.GET.get('id', '')
    if flower_id:
        # 获取上一个页面的ur1地址
        prev_url = request.META['HTTP_REFERER']
        response = redirect(prev_url)
        flower_count = request.COOKIES.get(flower_id, '')
        if flower_count:
            response.delete_cookie(flower_id)

    return response


def place_order(request):
    cart_flower_list = []
    cart_flower_count = 0
    cart_flower_money = 0
    # 从cookie里获职数据 商品的id:商品的敬量
    for flower_id, flower_num in request.COOKIES.items():
        if not flower_id.isdigit():
            continue
        # 根据id获取商品对象
        cart_flowers = flowerInfo.objects.get(id=flower_id)
        # 把商品的数量存到商品对象里
        cart_flowers.flower_num = flower_num  # 计算商品的小计价格 存到商品对象里
        cart_flowers.total_money = cart_flowers.flower_price * int(flower_num)
        # 把商品对象存到列表里
        cart_flower_list.append(cart_flowers)
        # 计算总的数量
        cart_flower_count += int(flower_num)
        # 累加总的价格
        cart_flower_money += cart_flowers.flower_price * int(flower_num)

    return render(request, 'place_order.html', {'cart_flower_list': cart_flower_list,
                                                'cart_flower_count': cart_flower_count,
                                                'cart_flower_money': cart_flower_money})


def submit_order(request):
    # 订单功能
    # 获生成订单需要的数据
    addr = request.POST.get('addr', '')
    recv = request.POST.get('recv', ' ')
    tele = request.POST.get('tele')
    extra = request.POST.get('extra')
    tim = request.POST.get('time','')
    # 实例化订单对象
    order_info = OrderInfo()  # 给订单赋值
    order_info.order_addr = addr
    order_info.order_tele = tele
    order_info.order_recv = recv
    order_info.order_extra = extra
    order_info.order_time = tim
    order_info.order_id = str(time.time())  # + str(time.clock() * 1000000)
    order_info.save()

    response = redirect('/cart/submit_success/?id=%s'%order_info.order_id)

    for flower_id, flower_num in request.COOKIES.items():
        if not flower_id.isdigit():
            continue
        cart_flowers = flowerInfo.objects.get(id=flower_id)
        order_flowers = OrderFlowers()
        order_flowers.flower_info = cart_flowers
        #order_flowers.flower_info_id = flower_id
        order_flowers.flower_num = flower_num
        order_flowers.flower_order = order_info
        order_flowers.save()

        response.delete_cookie(flower_id)

    return response


def submit_success(request):
    order_id = request.GET.get('id')
    orderinfo = OrderInfo.objects.get(order_id=order_id)
    # ordeninfo.ordergoods set
    order_flower_list = OrderFlowers.objects.filter(flower_order=orderinfo)
    # 总价
    total_money = 0
    # 总故量
    total_num = 0
    for flowers in order_flower_list:  # 商品价格小记
        flowers.total_money = flowers.flower_info.flower_price * flowers.flower_num
        total_money += flowers.total_money
        total_num = flowers.flower_num

    return render(request, 'success.html', {'orderinfo': orderinfo,
                                            'order_flower_list': order_flower_list,
                                            'total_money': total_money,
                                            'total_num': total_num})
