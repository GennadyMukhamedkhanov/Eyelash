from django.db import models


#  Услуга
class Service(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30, blank=False, null=True)
    description = models.TextField(verbose_name='Описание', blank=False, null=True)
    price = models.IntegerField(verbose_name='Цена', blank=False, null=True)
    image = models.ImageField(upload_to='/')


#  Расписани
class Shedule(models.Model):
    service = models.CharField(verbose_name='Описание услуги', max_length=100)
    date = models.TextField(verbose_name='xx.xx.xx xx.xx', max_length=14)


#  Бронирование
class Booking(models.Model):
    shedule = models.CharField(verbose_name='Описание услуги', max_length=100)
    user = models.CharField(verbose_name='Имя', max_length=30)
    status = models.BooleanField()

#  Время процедуры
class Time(models.Model):
    start_date = models.TextField(verbose_name='Начало времени процедуры', blank=False, null=True)
    end_date = models.TextField(verbose_name='Окончание времени процедуры', blank=False, null=True)


class User(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30)
    phone = models.CharField(verbose_name='Телефон', max_length=30)
    email_user = models.EmailField(max_length=50)