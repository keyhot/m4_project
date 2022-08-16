from django.shortcuts import render, HttpResponse
from .models import Bottle

# Create your views here.


def contacts(request):
    response = HttpResponse("<h1>Тел.: 0704776727</h1>")
    return response


def about(request):
    return render(request, 'about.html')


def makers_list(request):
    context = {}
    # SELECT * FROM Bottle
    bottles_list = Bottle.objects.all()
    context["bottles_list"] = bottles_list
    html_page = render(request, 'makers.html', context)
    return html_page