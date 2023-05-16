from .models import Category, Course
from django.contrib import admin


class CourseInline(admin.TabularInline):

    extra = 0

    fields = (
        'title',
        'category',
        'price',
        'student_quantity',
        'review_quantity'
    )

    model = Course


class CategoryAdmin(admin.ModelAdmin):

    fields = ['title']

    inlines = [CourseInline]

    list_display = ('id', 'title', 'created_at')

    list_display_links = ['title']


class CourseAdmin(admin.ModelAdmin):

    fields = (
        'title',
        'category',
        'price',
        'student_quantity',
        'review_quantity'
    )

    list_display = (
        'id',
        'title',
        'category',
        'price',
        'student_quantity',
        'review_quantity',
        'created_at'
    )

    list_display_links = ['title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
