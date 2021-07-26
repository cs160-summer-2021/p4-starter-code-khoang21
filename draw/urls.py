# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('bigscreen', views.bigscreen, name='bigscreen'),
    path('form', views.form, name='form'),

]
