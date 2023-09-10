from django.db import models


class Time(models.Model):
    start_date = models.DateTimeField(verbose_name='Начало времени процедуры')
    end_date = models.DateTimeField(verbose_name='Окончание времени процедуры')


    def __str__(self):
        return f'{self.start_date} {self.end_date}'

    class Meta:
        db_table = 'time'
        verbose_name = 'Время'
        verbose_name_plural = 'Время'
