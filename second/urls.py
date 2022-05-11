from django.urls import path, re_path

from . import views
# 현재 위치니깐 .

urlpatterns=[
    path('list/', views.list, name="list"),
    path('create/', views.create, name='create'),

]