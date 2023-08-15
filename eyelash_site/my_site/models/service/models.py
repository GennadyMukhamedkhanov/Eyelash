from django.db import models


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