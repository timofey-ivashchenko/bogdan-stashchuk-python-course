from api.resources import CategoryResource, CourseResource
from django.urls import include, path
from tastypie.api import Api

api = Api(api_name='v1')
api.register(CategoryResource())
api.register(CourseResource())

# /api/v1/categories/   GET
# /api/v1/categories/1/ GET
# /api/v1/courses/      GET, POST
# /api/v1/courses/1/    GET, DELETE

# Для методов POST и DELETE требуется авторизация с помощью ключа API.
# Ключ заголовка: Authorization
# Значение заголовка: ApiKey <username>:<api_key>

urlpatterns = [
    path('', include(api.urls), name='root')
]
