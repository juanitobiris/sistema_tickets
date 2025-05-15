from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Ticket(models.Model):
    ESTADOS = [
        ('abierto', 'Abierto'),
        ('proceso', 'En Proceso'),
        ('cerrado', 'Cerrado'),
    ]

    PRIORIDADES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='abierto')
    prioridad = models.CharField(max_length=10, choices=PRIORIDADES, default='media')
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_creados')
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tickets_asignados')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo