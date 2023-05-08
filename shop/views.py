from django.http import HttpResponse


def index(_):
    return HttpResponse('Hello from the Shop app!')
