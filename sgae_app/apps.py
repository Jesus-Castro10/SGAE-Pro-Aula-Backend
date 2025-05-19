from django.apps import AppConfig


class SgaeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sgae_app'


    def ready(self):
        from sgae_app.infrastructure.config.container import Container
        from sgae_project import settings
    
        global container
        container = Container()
        container.config.from_dict(settings.__dict__)

        container.wire(packages=[
            "sgae_app.interfaces.api",
            "sgae_app.application.services"
        ])
