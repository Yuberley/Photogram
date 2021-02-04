"""Module for Photogram"""

from django.urls import path
from Photogram import views as local_views
from posts import views as posts_views

def hello_world(requiest):
    """Return a greeting"""
    return HttpResponse('Hello, World')

urlpatterns = [
    path('hello_world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('posts/', posts_views.list_posts),
]
