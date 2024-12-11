from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuario(AbstractUser):
    correo = models.EmailField(unique=True)
    nivel = models.PositiveIntegerField(default=1)