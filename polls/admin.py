from django.contrib import admin
from .models import   Contact , Hotel,Category,Checkout
class AdminCategorie(admin.ModelAdmin):
    list_display=('name','date_added')

class AdminProduct(admin.ModelAdmin):
    list_display=('title','price','category','date_added')
admin.site.register(Contact)
admin.site.register(Checkout)

admin.site.register(Hotel,AdminProduct)
admin.site.register(Category,AdminCategorie)

# Register your models here.
