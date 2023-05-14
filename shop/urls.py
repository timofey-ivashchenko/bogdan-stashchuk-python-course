from . import views
from django.urls import path

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<int:course_id>', views.single_course, name='single_course')
]
