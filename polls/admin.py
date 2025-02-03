from django.contrib import admin
from .models import   Contact , Hotel,Category,Checkout,Flight,Reserver_vol
class AdminCategorie(admin.ModelAdmin):
    list_display=('name','date_added')

class AdminProduct(admin.ModelAdmin):
    list_display=('title','price','category','date_added')
admin.site.register(Contact)
admin.site.register(Checkout)
admin.site.register(Flight)
admin.site.register(Reserver_vol)
admin.site.register(Hotel,AdminProduct)
admin.site.register(Category,AdminCategorie)

