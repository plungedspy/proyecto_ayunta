from django.db import models
from django.contrib.auth.models import AbstractUser


class Puesto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    # Jerarquía: un puesto puede tener un superior
    superior = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='subordinados'
    )

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    

class Usuario(models.Model):
    
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    correo = models.CharField(max_length=100, null=True, blank=True)
    puesto = models.ForeignKey(
        Puesto,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Create your models here.
