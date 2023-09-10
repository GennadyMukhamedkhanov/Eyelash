from django.db import models


#  Расписаниe
class Shedule(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE,
                                verbose_name='Услуга')
    date = models.ForeignKey('Time', on_delete=models.CASCADE,
                             verbose_name='Время проведения услуги')
    status = models.BooleanField(default=False,
                                 verbose_name='Статус расписания')

    def __str__(self):
        return f'{self.service.name} {self.date.start_date}  '

    class Meta:
        db_table = 'shedule'
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
