from shop.models import Category, Course
from tastypie.resources import ModelResource


class CategoryResource(ModelResource):

    class Meta:

        allowed_methods = ['get']

        queryset = Category.objects.all()

        resource_name = 'categories'


class CourseResource(ModelResource):

    class Meta:

        allowed_methods = ['delete', 'get', 'post']

        queryset = Course.objects.all()

        resource_name = 'courses'
