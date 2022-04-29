"""swiftbuy_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from user import views as user_views

urlpatterns = [
    path('', views.sellinfo),
    path('/addproduct', views.addproduct),
    path('/selling', views.selling),
    path('/update/<int:productid>', views.update, name='addreview'),
    path('/delete/<int:productid>', views.delete, name='addreview'),
    path('/history', views.history, name='history'),
    path('/analytics', views.analytics, name='analytics'),
]
