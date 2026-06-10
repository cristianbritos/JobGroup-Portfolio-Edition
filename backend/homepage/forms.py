from datetime import datetime

from django import forms

from .models import Mensaje


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'correo', 'asunto', 'mensaje']
