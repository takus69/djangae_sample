"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.staticfiles import views

# Add for admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^_ah/', include('djangae.urls')),
    # Modify for admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', include('hello.urls')),
    url(r'^polls/', include('polls.urls')),
    # Add for admin
    url(r'^auth/', include('djangae.contrib.gauth.urls')),
]

# Apply only when DEBUG is True.
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
 urlpatterns += [
   url(r'^images/(?P<path>.*)$', views.serve),
 ]
