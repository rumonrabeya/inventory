from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('display_host/', display_host, name='display_host'),
    path('display_vm/', display_vm, name='display_vm'),
    path('add_host/', add_host, name='add_host'),
    path('add_vm/', add_vm, name='add_vm'),
    path('edit_host/<pk>', edit_host, name='edit_host'),
    path('edit_vm/<pk>', edit_vm, name='edit_vm'),
    path('delete_host/<pk>', delete_host, name='delete_host'),
    path('delete_vm/<pk>', delete_vm, name='delete_vm'),
    path('container_items/<pk>', container_items, name='container_items'),
    path('search/', search, name='search'),
    path('dc_items/', dc_items, name='dc_items'),
    path('dr_items/', dr_items, name='dr_items'),
    path('far_dr_items/', far_dr_items, name='far_dr_items'),
    path('about/', about, name='about'),

]