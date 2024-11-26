from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),  
    path('', views.index, name='index'),  
]
