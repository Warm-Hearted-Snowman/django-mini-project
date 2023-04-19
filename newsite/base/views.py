from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


def light_page(request):
    return render(request, 'message.html')


def home_page(request):
    return render(request, 'Welcome Page.html')


def show_time(request):
    return HttpResponse(datetime.now())
