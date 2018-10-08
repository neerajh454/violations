"""violations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers, viewsets

#from django.contrib import admin
#from django.contrib.auth.models import User

from . import views

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


urlpatterns = [
    #url(r'^', include(router.urls)),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    ## -- Link to Types urls.py -- ##
    url(r'^types/view/$', views.view_types, name="types_vio.view"),
    url(r'^types/add/$', views.violation_types, name="types_vio.add"),

    url(r'^violations/$', views.ViolationData.as_view()), ## -- Link to Violation functions -- ##
    #url(r'^violations/', views.violation_data, name='violations.violation'), ## -- Link to Violation functions -- ##
    
    ## -- Link to Actions urls.py -- ##
    url(r'^actions/view/$', views.ViewActionData.as_view(), name="actions.view"),
    url(r'^actions/add/$', views.SetActionData.as_view(), name="actions.add"),

    ## -- Link to Comments urls.py -- ##
    url(r'^comments/view/$', views.ViewCommentData.as_view(), name="comments.view"),
    url(r'^comments/add/$', views.SetCommentData.as_view(), name="comments.add"),

    
]