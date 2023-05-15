"""
URL configuration for `base` project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Examples:

Function views
1. Add an import:
    from my_app import views
2. Add a URL to `urlpatterns`:
    path('', views.home, name='home')

Class-based views
1. Add an import:
    from other_app.views import Home
2. Add a URL to `urlpatterns`:
    path('', Home.as_view(), name='home')

Including another URL configuration
1. Import the `include` function:
    from django.urls import include, path
2. Add a URL to `urlpatterns`:
    path('blog/', include('blog.urls'))
"""

from api.resources import CategoryResource, CourseResource
from django.contrib import admin
from django.urls import include, path
from tastypie.api import Api

api = Api(api_name='v1')
api.register(CategoryResource())
api.register(CourseResource())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api.urls)),
    path('shop/', include('shop.urls')),
]
