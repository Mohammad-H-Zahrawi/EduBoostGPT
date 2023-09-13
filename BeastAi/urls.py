"""BeastAi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

# from django.conf.urls import url
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'), 
    path('projects/', include('projects.urls')),
    path('donate/', views.donate, name='donate'),
    path('cancel/', views.cancel, name='cancel'),

    path('success/', views.success, name='success'),
    path('thankyouforsubmitting/', views.thankyouforsubmitting, name='thankyouforsubmitting'),
    path('hii/', views.hii, name='hii'),
        # path('hii/recording', views.record, name='record')




]

