from django.urls import path, re_path
#from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^accounts/register/?$', views.register, name='register'),
    re_path(r'^submit/expense/', views.submit_expense, name='submit_expense'),
    re_path(r'^$', views.index, name='index'),
]