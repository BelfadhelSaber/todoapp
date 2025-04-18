<<<<<<< HEAD
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
=======
from django.urls import path

from . import views

urlpatterns = [
    
    path("index", views.index, name="index"),
    path("",views.bienvenu,name='bienvenu'),
    path("login",views.loginpage,name='login'),
    path("signup",views.signup,name="signup"),
    path("hotels",views.hotel,name='home'),
    path("flight_list",views.flight_list,name='flight_list'),
    path('reserver_vol', views.reserver_vol, name='reserver_vol'),
    path('reservation/success/', views.reservation_success, name='reservation_success'),

    path('<int:myid>',views.detail,name='detail'),
    path('checkout/<int:hotel_id>',views.checkout,name='checkout'),
    path("contact",views.contact,name='contact'),
    path('logout/',views.LogoutView,name='logout'),
    path('set_language',views.set_language,name='set_language'),
]
>>>>>>> master
