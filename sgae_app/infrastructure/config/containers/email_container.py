from dependency_injector import containers, providers

from sgae_app.application.services.email_sender_service import EmailSenderService
from sgae_app.application.services.user_registration_notifier import UserRegistrationNotifier

class EmailContainer(containers.DeclarativeContainer):
    email_sender_service = providers.Singleton(EmailSenderService)
    user_notifier = providers.Factory(UserRegistrationNotifier, email_sender_service=email_sender_service)
