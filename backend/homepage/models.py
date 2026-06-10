from datetime import datetime
from django.db import models
from django.forms.models import model_to_dict

# Create your models here.


class Mensaje(models.Model):
    nombre = models.CharField(max_length=300)
    correo = models.EmailField()
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha = models.DateField(default=datetime.now, verbose_name='Fecha')
    estado = models.BooleanField(default=False)  # Valor por defecto

    def __str__(self) -> str:
        return '{} ({})'.format(self.nombre, self.asunto)

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ['id']
