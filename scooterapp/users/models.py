from django.db import models
from django.contrib.auth.models import AbstractUser



#Расширил базовый User для того, чтобы пользователи при регистрации писали свой город и, если хотят загружали свои аватарки
class CustomUser(AbstractUser):
    city = models.CharField(max_length=255, null=False, default='')
    img = models.ImageField(upload_to='avatar', null=False, blank=False)