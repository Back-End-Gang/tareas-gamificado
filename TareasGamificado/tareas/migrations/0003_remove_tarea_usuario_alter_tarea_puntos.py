# Generated by Django 5.1.1 on 2024-12-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_tarea_logro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='tarea',
            name='puntos',
            field=models.PositiveIntegerField(default=1),
        ),
    ]