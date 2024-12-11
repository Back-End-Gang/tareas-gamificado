"""
URL configuration for TareasGamificado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from tareas.views import crear_tarea, listar_tareas, actualizar_tarea, eliminar_tarea, pagina_inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_inicio, name='inicio'),  # Página de inicio
    path('crear/', crear_tarea, name='crear_tarea'),
    path('listar/', listar_tareas, name='listar_tareas'),
    path('actualizar/<int:id>/', actualizar_tarea, name='actualizar_tarea'),
    path('eliminar/<int:id>/', eliminar_tarea, name='eliminar_tarea'),
]