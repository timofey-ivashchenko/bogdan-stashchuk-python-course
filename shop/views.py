from .models import Course
# from django.http import Http404
from django.shortcuts import get_object_or_404, render


def index(request):
    courses = Course.objects.all()
    return render(
        request=request,
        template_name='courses.html',
        context={'courses': courses}
    )


def single_course(request, course_id):
    # Вариант 1

    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(
    #         request=request,
    #         template_name='single_course.html',
    #         context={'course': course}
    #     )
    # except Course.DoesNotExist:
    #     raise Http404()

    # Вариант 2

    course = get_object_or_404(Course, pk=course_id)
    return render(
        request=request,
        template_name='single_course.html',
        context={'course': course}
    )
