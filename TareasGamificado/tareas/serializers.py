from rest_framework import serializers
from .models import Tarea
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer

class TareaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer
    usuario_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), source='usuario', write_only=True)

    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'descripcion', 'estado', 'puntos', 'usuario', 'usuario_id']