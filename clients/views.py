from django.shortcuts import render, HttpResponse
from .models import Client, Order
from .forms import OrderForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View

# Create your views here.


class ClientListView(ListView):
    model = Client
    template_name = 'clients/clients.html'


class OrderListView(ListView):
    model = Order
    template_name = 'clients/orders.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = "clients/order_details.html"


class OrderUpdateView(UpdateView):
    model = Order
    fields = ["name", "contacts", "description"]
    template_name_suffix = '_update'
    success_url = "/orders/"


class OrderDeleteView(DeleteView):
    model = Order
    success_url = "/orders/"


class CreateOrderView(CreateView):
    model = Order
    template_name = 'clients/order_djangoform.html'
    fields = ["name", "contacts", "description"]
    success_url = "/orders/"
