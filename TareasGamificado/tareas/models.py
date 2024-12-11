from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Tarea(models.Model):
    ESTADOS = [('pendiente', 'Pendiente'), ('completada', 'Completada')]
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    puntos = models.PositiveIntegerField(default=0)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, related_name="tareas")

