from django.db import models

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
