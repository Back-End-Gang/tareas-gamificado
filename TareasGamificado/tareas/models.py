from django.db import models
from usuarios.models import Usuario  # Importa el modelo de usuario extendido
from logros.models import Logro

class Tarea(models.Model):
    ESTADOS = [('pendiente', 'Pendiente'), ('completada', 'Completada')]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    puntos = models.PositiveIntegerField(default=0)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,  # Permitir valores nulos
        related_name="tareas"  # Relación reverse
    )
    logro = models.ForeignKey(Logro, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo