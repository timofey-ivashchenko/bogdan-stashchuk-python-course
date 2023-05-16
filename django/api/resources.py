from .authentication import CustomAuthentication
from shop.models import Category, Course
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource


class CategoryResource(ModelResource):

    class Meta:

        allowed_methods = ['get']

        queryset = Category.objects.all()

        resource_name = 'categories'


class CourseResource(ModelResource):

    class Meta:

        allowed_methods = ['delete', 'get', 'post']

        authentication = CustomAuthentication()

        authorization = Authorization()

        queryset = Course.objects.all()

        resource_name = 'courses'

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category_title'] = bundle.obj.category.title
        return bundle

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle
