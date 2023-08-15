from django.db import models


#  Расписаниe
class Shedule(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name='Услуга')
    date = models.ForeignKey('Time', on_delete=models.CASCADE, verbose_name='Время проведения услуги')

    def __str__(self):
        return f'{self.service.name} {self.data.start_date} - {self.data.end_date}'

    class Meta:
        db_table = 'shedule'
        verbose_name = 'Время'
        verbose_name_plural = 'Время'

