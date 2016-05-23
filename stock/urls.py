"""stock URL Configuration

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
from django.conf.urls import include, url , patterns
from django.contrib import admin

#from django.views.generic.create_update import create_object, update_object
from stockapp.models import Product
from stockapp.forms import ProductForm


"""
urlpatterns = patterns('',

url(r'^new/$', create_object, {'form_class': ProductForm,
        'post_save_redirect': '/'}, name='create_product'),


)
"""



urlpatterns = [
	url(r'^polls/',include('stockapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
