"""Posts views"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

# Create your views here.

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yuberley Guerrero',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]

def list_posts(request):
    """List existing posts"""
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><strong>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))