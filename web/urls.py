from django.urls import path, re_path
#from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^submit/expense/', views.submit_expense, name='submit_expense')
]