from django.db import models
from my_site import *


class Booking(models.Model):
    shedule = models.ForeignKey('Shedule', on_delete=models.CASCADE,
                                verbose_name='Услуга', related_name='bookings')
    user = models.ForeignKey('User', on_delete=models.CASCADE,
                             verbose_name='Пользователь', related_name='bookings')
    status = models.BooleanField(default=False, verbose_name='Одобрено')

    def __str__(self):
        return f'{self.shedule.service.name} {self.user.username}'

    class Meta:
        db_table = 'booking'
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
        ordering = ['shedule', 'user']
        # ordering сортировка сначала по первому элементу shedule
        # если по первому элементу значения равны сотрируется по второму
        # можно указывать больше трех значений для сортировки
        # если указать '-shedule' со знаком минус, сортировка в обратной последовательности
