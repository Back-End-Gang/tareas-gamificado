from django.db import models
from .models import Usuario
# Create your models here.
class Logro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, related_name="logros")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()