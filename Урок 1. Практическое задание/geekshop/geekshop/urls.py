"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# из модуля django.contrib импортируется класс AdminSite, который предоставляет возможности работы
# с интерфейсом администратора
from django.contrib import admin    # Стандартная админка django (способна администрировать сайт)
# из модуля django.urls импортируется функция path. Эта функция задает сопоставление определенного
# маршрута с функцией обработки
from django.urls import path, include        # Метод с помощью которого определяются урлы

import mainapp.views as mainapp
# from mainapp import views - второй вариант

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', mainapp.main, name='main'),                    # корневой url
    path('products/', include('mainapp.urls', namespace='products')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('admin/', include('adminapp.urls', namespace='admin')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
