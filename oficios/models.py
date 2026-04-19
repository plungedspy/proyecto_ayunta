from django.db import models
from django.conf import settings

class Oficio(models.Model):
    folio_recepcion = models.CharField(max_length=20, null= True, blank=True)
    folio_dependencia = models.CharField(max_length=20, null= True, blank=True)
    folio_interno = models.CharField(max_length=20, null= True, blank=True)
    asunto = models.CharField(max_length=260)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_recibido = models.DateTimeField(null=True, blank=True)
    fecha_enviado = models.DateTimeField(null=True, blank=True)
    
    ESTADOS = [
        ('RECIBIDO','Recibido'),
        ('ENVIADO','Enviado'),
        ('PENDIENTE', 'Pendiente'),
    ]

    estado = models.CharField(max_length=20,
        choices = ESTADOS, default ='PENDIENTE')

    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name='oficios')

    remitente = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.asunto
# Create your models here.
