from django.shortcuts import render, HttpResponse
from .models import Client

# Create your views here.


def clients_list(request):
    context = {}
    customer_list = Client.objects.all()
    context["clients_list"] = customer_list
    html_page = render(request, 'clients/clients.html', context)
    return html_page
