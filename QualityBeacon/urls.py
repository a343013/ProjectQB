"""
URL configuration for MyEvaluation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from evaluation.views import index, registrar, consultar, modificar, crear_agente, crear_inspector, crear_evaluacion, editar_agente, editar_inspector, editar_evaluacion, eliminar_agente, eliminar_inspector, eliminar_evaluacion



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registrar/', registrar, name='registrar'),
    path('consultar/', consultar, name='consultar'),
    path('modificar/', modificar, name='modificar'),
    path('crear_agente/', crear_agente, name='crear_agente'),
    path('crear_inspector/', crear_inspector, name='crear_inspector'),
    path('crear_evaluacion/', crear_evaluacion, name='crear_evaluacion'),
    path('editar_agente/<int:pk>/', editar_agente, name='editar_agente'),
    path('editar_inspector/<int:pk>/', editar_inspector, name='editar_inspector'),
    path('editar_evaluacion/<int:pk>/', editar_evaluacion, name='editar_evaluacion'),
    path('eliminar_agente/<int:pk>/', eliminar_agente, name='eliminar_agente'),
    path('eliminar_inspector/<int:pk>/', eliminar_inspector, name='eliminar_inspector'),
    path('eliminar_evaluacion/<int:pk>/', eliminar_evaluacion, name='eliminar_evaluacion'),


]
