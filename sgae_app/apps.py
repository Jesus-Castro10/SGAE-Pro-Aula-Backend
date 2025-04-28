from django.apps import AppConfig


class SgaeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sgae_app'

    def ready(self):
        import sgae_app.infrastructure.models.student
