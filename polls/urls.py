from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login",views.loginpage,name='login'),
    path("signup",views.signup,name="signup"),
    path("home",views.hotel,name='home'),
    path("detail",views.detail,name='detail'),
    path("bienvenu",views.bienvenu,name='bienvenu'),
    path('checkout/<int:hotel_id>',views.checkout,name='checkout'),
    path("contact",views.contact,name='contact'),
    path('logout/',views.LogoutView,name='logout'),
    path('set_language',views.set_language,name='set_language'),


]
