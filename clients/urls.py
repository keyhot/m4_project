from django.urls import path

from . import views

urlpatterns = [
    path('clients/', views.ClientListView.as_view(), name='clients'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('order/update/<int:pk>/', views.OrderUpdateView.as_view(), name='order-update'),
    path('order/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order-delete'),
    path('order/djangoform/', views.CreateOrderView.as_view(), name='order-djangoform'),
]