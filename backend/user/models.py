from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.forms import model_to_dict

from crum import get_current_request

from config.settings import MEDIA_URL, STATIC_URL


class User(AbstractUser):
    class Types(models.IntegerChoices):
        ADMIN = 0, 'Administrador'
        TEACHER = 1, 'Profesor'
        STUDENT = 2, 'Estudiante'

    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
    token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)
    telefono = models.CharField(max_length=100, verbose_name='Teléfono')
    legajo = models.IntegerField(default=0, verbose_name='Legajo')
    tipo =  models.IntegerField(choices=Types.choices, default=Types.STUDENT, verbose_name='Tipo de Usuario')
    email = models.EmailField(unique=True)
 
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def get_full_name(self):
        return '{}, {}'.format(self.last_name, self.first_name)

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        item['full_name'] = self.get_full_name()
        return item
    
    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass


 
