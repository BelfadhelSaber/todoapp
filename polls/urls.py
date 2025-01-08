from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login",views.loginpage,name='login'),
    path("signup",views.signup,name="signup"),
    path("home",views.home,name='home'),
    path("todo",views.todo,name='todo'),
    path("deletetodo/<int:todo_id>",views.deletetodo,name='deletetodo'),
    path("contact",views.contact,name='contact'),
    path('logout/',views.LogoutView,name='logout'),
    path('set_language',views.set_language,name='set_language'),


]
