from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    telefono = models.CharField('Télefono', max_length=15)
    avatar = models.ImageField('avatar para tu perfil', upload_to='cover/', blank=True, null=True)
    fondo = models.ImageField('Elige tu fondo de perfil', upload_to='cover/', blank=True, null=True)

    class Meta:
        db_table = 'auth_user'