from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('unidad1/',views.unidad1,name='unidad1'),
    path('unidad2/',views.unidad2,name='unidad2'),
    path('unidad3/',views.unidad3,name='unidad3'),
    path('unidad4/',views.unidad4,name='unidad4'),
    path('unidad5/',views.unidad5,name='unidad5'),
    path('arduino/',views.arduino,name='arduino'),
    path('rp2040/',views.rp2040,name='rp2040'),

]