# Generated by Django 4.2.4 on 2024-01-08 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0006_alter_booking_shedule_alter_booking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shedule',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shedule', to='my_site.service', verbose_name='Услуга'),
        ),
    ]
