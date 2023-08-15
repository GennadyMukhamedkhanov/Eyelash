from django.contrib.auth.models import AbstractUser
from django.db import models


#  Услуга
class Service(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.IntegerField(blank=False, null=True, verbose_name='Цена')
    image = models.ImageField(upload_to='service/', verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'service'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


#  Расписаниe
class Shedule(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name='Услуга')
    date = models.ForeignKey('Time', on_delete=models.CASCADE, verbose_name='Время проведения услуги')

    def __str__(self):
        return f'{self.service.name} {self.data.start_date} - {self.data.end_date}'

    class Meta:
        db_table = 'time'
        verbose_name = 'Время'
        verbose_name_plural = 'Время'


#  Бронирование
class Booking(models.Model):
    shedule = models.ForeignKey('Shedule', on_delete=models.CASCADE, verbose_name='Услуга')
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.BooleanField(default=False, verbose_name='Одобрено')

    def __str__(self):
        return f'{self.shedule.service.name} {self.user.username}'

    class Meta:
        db_table = 'booking'
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'


#  Время процедуры
class Time(models.Model):
    start_date = models.TextField(verbose_name='Начало времени процедуры')
    end_date = models.TextField(verbose_name='Окончание времени процедуры')

    def __str__(self):
        return f'{self.start_date} {self.end_date}'

    class Meta:
        db_table = 'time'
        verbose_name = 'Время'
        verbose_name_plural = 'Время'


class User(AbstractUser):
    phone = models.CharField(max_length=14, verbose_name='Телефон')

    def __str__(self):
        return f'{self.username} {self.phone}'

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
