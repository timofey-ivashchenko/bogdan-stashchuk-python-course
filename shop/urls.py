from . import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
    # Список всех курсов.
    path('', views.courses, name='index'),
    # Страница отдельного курса.
    path('course/<int:course_id>', views.single_course, name='single_course')
]
