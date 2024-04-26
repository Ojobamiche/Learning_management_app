# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('select/', views.select_course, name='select_course'),
    path('display/', views.display_selected_course, name='display_selected_course'),
]
# views.py  
# from django.shortcuts import render
#