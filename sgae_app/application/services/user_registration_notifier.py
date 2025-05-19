from sgae_app.application.services.email_sender_service import EmailSenderService
import logging

class UserRegistrationNotifier:
    def __init__(self, email_sender_service):
        self.email_sender_service = email_sender_service
        self.logger = logging.getLogger('sgae_app')

    def notify_user(self, user_obj):
        email = getattr(user_obj, 'email', None)
        first_name = getattr(user_obj, 'first_name', '')
        second_name = getattr(user_obj, 'second_name', '')
        if not email:
            self.logger.error("No se pudo enviar el correo: el usuario no tiene email.")
            return False
        email_sent = self.email_sender_service.send_registration_confirmation_email(
            user_email=email,
            first_name=first_name,
            second_name=second_name,
        )
        if not email_sent:
            self.logger.error(f"No se pudo enviar el correo de confirmación a {email}")
        return email_sent