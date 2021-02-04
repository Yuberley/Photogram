"""Photogram views"""

#Django
from django.http import HttpResponse
from django.http import JsonResponse
import json

#Utilities
from datetime import datetime


def hello_world(request):
    """Return a greeting"""

    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello, current server time is {now}'.format(now=str(now)))

def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'massage': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )

def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Photogram'.format(name)

    return HttpResponse(message)