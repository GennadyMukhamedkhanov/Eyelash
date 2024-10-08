# Generated by Django 4.2.4 on 2024-01-08 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0005_remove_time_status_shedule_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='shedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='my_site.shedule', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
