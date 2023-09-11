"""flowershop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from cart.views import add_cart, show_cart, remove_cart, place_order, submit_order, submit_success
from django.contrib import admin
from django.urls import path, include
from goods.views import index, detail, flower

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.url')),
    path('goods/', index),
    path('index/', index),
    #path('user/(?P<pk>\d+)/cart/add_cart/', add_cart),
    path('cart/', index),
    path('detail/', detail),
    path('cart/add_cart/', add_cart),
    path('flower/', flower),
    path('cart/show_cart/', show_cart),
    path('cart/remove_cart/', remove_cart),
    path('cart/place_order/', place_order),
    path('cart/submit_success/', submit_success),
    path('cart/submit_order/', submit_order),

]
