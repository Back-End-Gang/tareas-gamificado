from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    correo = models.EmailField(unique=True)
    nivel = models.PositiveIntegerField(default=1)
    groups = models.ManyToManyField(Group, related_name="usuarios_groups", blank=True, help_text="The groups this user belongs to.", verbose_name="groups")
    user_permissions = models.ManyToManyField(Permission, related_name="usuarios_permissions", blank=True, help_text="Specific permissions for this user.", verbose_name="user permissions")

    def __str__(self):
        return self.username
