# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('bigscreen', views.bigscreen, name='bigscreen'),
    path('form', views.form, name='form'),
    path('manager', views.manager, name='manager'),
    path('busser', views.busser, name='busser'),
    path('chef', views.chef, name='chef'),
    path('cashier', views.cashier, name='cashier'),
    path('host', views.host, name='host'),
    path('server', views.server, name='server'),

]
