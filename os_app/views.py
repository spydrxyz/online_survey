from django.views import generic
from django.shortcuts import render


def index(request):
    return render(request, 'os_app/index.html')


def surveylist(request):
    return render(request, 'os_app/surveylist.html')
