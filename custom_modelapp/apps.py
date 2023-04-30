from django.apps import AppConfig


class CustomModelappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_modelapp'
