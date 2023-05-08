from .models import Course
from django.http import HttpResponse


def index(_):
    return HttpResponse(''.join(f'{x}<br>' for x in Course.objects.all()))
