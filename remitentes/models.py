from django.db import models

class Remitente(models.Model):
    TIPO_CHOICES = [
        ('CIUDADANO', 'Ciudadano'),
        ('DEPENDENCIA', 'Dependencia'),
        ('DIRECCION', 'Direccion'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
# Create your models here.
