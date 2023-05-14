from .models import Course
from django.shortcuts import render


def index(request):
    courses = Course.objects.all()
    return render(
        request=request,
        template_name='courses.html',
        context={'courses': courses}
    )


def single_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(
        request=request,
        template_name='single_course.html',
        context={'course': course}
    )
