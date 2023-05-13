from .models import Course
from django.shortcuts import render


def index(request):
    return render(
        request=request,
        template_name='courses.html',
        context={'courses': Course.objects.all()})
