from django.shortcuts import render, HttpResponse
from .models import Client, Order
from .forms import OrderForm

# Create your views here.


def clients_list(request):
    context = {}
    customer_list = Client.objects.all()
    context["clients_list"] = customer_list
    html_page = render(request, 'clients/clients.html', context)
    return html_page


def orders_list(request):
    context = {}
    order_list = Order.objects.all()
    context["orders_list"] = order_list
    html_page = render(request, 'clients/orders.html', context)
    return html_page


def order_detail(request, id):
    context = {
        "order": Order.objects.get(id=id)
    }
    return render(request, 'clients/order_details.html', context)


def order_update(request, id):
    context = {}
    order_object = Order.objects.get(id=id)
    if request.method == "POST":
        form = OrderForm
    context["form"] = OrderForm(instance=order_object)
    return render(request, 'clients/order_update.html', context)


def order_delete(request, id):
    context = {}
    order_object = Order.objects.get(id=id)
    context['order'] = Order
    order_object.delete()
    return render(request, 'clients/order_deletion.html', context)


def order_djangoform(request):
    context = {}
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return HttpResponse("Форма обработана")
        return HttpResponse("Данные не валидны")
    context["order_form"] = OrderForm()
    return render(request, 'clients/order_djangoform.html', context)