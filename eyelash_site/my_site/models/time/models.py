from django.db import models


class Time(models.Model):
    start_date = models.DateTimeField(verbose_name='Начало времени процедуры')
    end_date = models.DateTimeField(verbose_name='Окончание времени процедуры')
    status = models.CharField(verbose_name='Статус записи', max_length=10, blank=True)

    def __str__(self):
        return f'{self.start_date} {self.end_date} {self.status}'

    class Meta:
        db_table = 'time'
        verbose_name = 'Время'
        verbose_name_plural = 'Время'
