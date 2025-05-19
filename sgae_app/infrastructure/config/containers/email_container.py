from dependency_injector import containers, providers

from sgae_app.infrastructure.services.email_user_notifier import EmailUserNotifier
from sgae_app.interfaces.external.user_notifier_interface import UserNotifierInterface  # opcional, solo para claridad

class EmailContainer(containers.DeclarativeContainer):
    user_notifier = providers.Singleton(EmailUserNotifier)
