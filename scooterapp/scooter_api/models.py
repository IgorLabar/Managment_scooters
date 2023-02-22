from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Класс Scooter - таблица в БД для самокатов
class Scooter(models.Model):
    STATUS = (
        ('Free', 'Свободный'),
        ('Charge', 'Заряжается'),
        ('Repair', 'На ремонте'),
        ('Is used', 'Используется'),
    )
    serial_number = models.CharField("Номер самоката",max_length=6, unique=True)
    latitude = models.FloatField("Широта", null=False)
    longitude = models.FloatField('Долгота',null=False)
    charge = models.CharField('Заряд',null=False, max_length=4)
    active = models.CharField('Статус',
        default='Free', max_length=255, null=False, blank=False, choices=STATUS)

    def __str__(self):
        return self.serial_number


# Trip - таблица в БД для поездок
class Trip(models.Model):
    cost = models.FloatField("Стоимость поездки")
    date_of_trip = models.DateField('Дата поездки')
    rider = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, db_index=True)
    scooter = models.ForeignKey(Scooter, on_delete=models.CASCADE)

    def __str__(self):
        return self.rider.user.username
