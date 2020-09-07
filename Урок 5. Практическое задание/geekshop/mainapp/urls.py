from django.urls import path
import mainapp.views as mainapp

# необходимо указывать app_name. Это требование функции include
app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('category/<int:pk>/<int:page>', mainapp.products, name='page'),       # страница передана
    path('product/<int:pk>/', mainapp.product, name='product'),                 # страница не передана
]
