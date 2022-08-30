from django.shortcuts import render, HttpResponse
from .models import Client

# Create your views here.


def index(request):
    return HttpResponse('<h1>Здравствуйте, вы находитесь на сайте WATER</h1>')


def contacts(request):
    response = HttpResponse("<h1>Тел.: 0704776727</h1>")
    return response


def about(request):
    return render(request, 'clients/about.html')


def clients_list(request):
    context = {}
    customer_list = Client.objects.all()
    context["clients_list"] = customer_list
    html_page = render(request, 'clients/clients.html', context)
    return html_page
