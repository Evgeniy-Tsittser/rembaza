from django.apps import AppConfig


class RembazaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rembaza_app'

    def ready(self):
        """Загрузка функций обработчиков сигнала при старте приложения"""
        from .signals import update_aggregate_tables
        from .signals import calculate_totals
        from .signals import delete_from_aggregate_tables
