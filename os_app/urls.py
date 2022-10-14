from unicodedata import name
from django.urls import path
from . import views

app_name = 'os_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('survey-list/', views.surveylist, name='surveylist')
]
