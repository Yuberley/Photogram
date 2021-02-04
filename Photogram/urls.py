"""Module for Photogram"""

from django.urls import path
from Photogram import views

def hello_world(requiest):
    """Return a greeting"""
    return HttpResponse('Hello, World')

urlpatterns = [
    path('hello_world/', views.hello_world),
    path('sorted/', views.sort_integers),
    path('hi/<str:name>/<int:age>/', views.say_hi),
]
