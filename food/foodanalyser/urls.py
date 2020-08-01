from django.conf.urls import url
from django.urls import path,include
from .import views

urlpatterns=[
    path(r'',views.login,name='login'),
    path(r'firstpage',views.firstpage,name='firstpage'),
    path(r'search',views.search,name='search'),
]