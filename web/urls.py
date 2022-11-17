from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include

from . import views
import web

app_name='web'

urlpatterns = [
    path('', views.WebIndex),
    path('WebIndex/', views.WebIndex, name='WebIndex'),
    path('Accounting/', views.Accounting, name='Accounting'),
    path('Finance/', views.Finance, name='Finance'),
    path('Language/', views.Language, name='Language'),
    path('Ins-Accounting/', views.InsAccounting, name='Ins-Accounting'),
    path('Ins-Finance/', views.InsFinance, name='Ins-Finance'),
    path('Ins-Language/', views.InsLanguage, name='Ins-Language'),
    path('class/', views.Class, name='class'),
    path('profile/<str:stu_name>', views.Profile, name='profile'),
    path('editprofile/<str:stu_name>', views.EditProfile, name='editprofile'),
]