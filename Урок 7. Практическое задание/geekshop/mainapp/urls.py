from django.urls import re_path
import mainapp.views as mainapp
from django.views.decorators.cache import cache_page

# необходимо указывать app_name. Это требование функции include
app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.products, name='index'),

    re_path(r'^category/(?P<pk>\d+)/$', mainapp.products, name='category'),
    re_path(r'^category/(?P<pk>\d+)/ajax/$', cache_page(3600)(mainapp.products_ajax)),
    re_path(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.products, name='page'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/ajax/$', cache_page(3600)(mainapp.products_ajax)),
]
