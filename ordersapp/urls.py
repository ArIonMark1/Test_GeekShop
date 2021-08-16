from django.urls import path

import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='order_list'),
    path('create/', ordersapp.OrderItemCreate.as_view(), name='order_create'),
    path('read/<pk>/', ordersapp.OrderList.as_view(), name='order_read'),
    path('update/<pk>/', ordersapp.OrderList.as_view(), name='order_update'),
    path('delete/<pk>/', ordersapp.OrderList.as_view(), name='order_delete'),

]
