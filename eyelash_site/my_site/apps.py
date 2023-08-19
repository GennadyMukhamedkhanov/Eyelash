from django.apps import AppConfig


class MySiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_site'
    verbose_name = 'Наращивание прекрасных ресниц'
    # verbose_name сработает если при регистрации уазали
    # полный путь приложения 'my_site.apps.MySiteConfig'
