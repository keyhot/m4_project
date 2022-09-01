from django.urls import path

from . import views

urlpatterns = [
    path('clients/', views.clients_list, name='clients'),
    path('orders/', views.orders_list, name='orders'),
    path('order/<int:id>/', views.order_detail, name='order-detail'),
    path('order/update/<int:id>/', views.order_update, name='order-update'),
    path('order/delete/<int:id>/', views.order_delete, name='order-delete'),
    path('order/djangoform/', views.order_djangoform, name='order-djangoform'),
]