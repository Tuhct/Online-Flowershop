from django.contrib import admin
from goods.models import flowerInfo,flowersCategory

# Register your models here.
class Finforadmin(admin.ModelAdmin):
    list_display = ['id','flower_name','flower_price','flower_desc']
    list_per_page = 20
    search_fields = ['id','flower_name']
admin.site.register(flowerInfo,Finforadmin)
admin.site.register(flowersCategory)