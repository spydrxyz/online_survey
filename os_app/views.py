from django.shortcuts import render


def index(request):
    return render(request, 'os_app/index.html')


def surveylist(request):
    return render(request, 'os_app/surveylist.html')


def studentauth(request):
    return render(request, 'os_app/studentauth.html')


def survey(request):
    return render(request, 'os_app/survey.html')


def surveyend(request):
    return render(request, 'os_app/surveyend.html')
