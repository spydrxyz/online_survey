from django.urls import path
from . import views

app_name = 'os_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('survey-list/', views.surveylist, name='surveylist'),
    path('student-auth/', views.studentauth, name='studentauth'),
    path('survey/', views.survey, name='survey'),
    path('survey-end/', views.surveyend, name='surveyend')
]
