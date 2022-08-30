from django.shortcuts import render, HttpResponse
from .models import Bottle


def contacts(request):
    return render(request, 'core/contacts.html')


def about(request):
    return render(request, 'core/about.html')


def makers_list(request):
    context = {}
    bottles_list = Bottle.objects.all()
    context["bottles_list"] = bottles_list
    html_page = render(request, 'core/makers.html', context)
    return html_page


def index(request):
    return render(request, 'index.html')
