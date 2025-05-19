from sgae_app.interfaces.external.user_notifier_interface import UserNotifierInterface
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import logging


class EmailUserNotifier(UserNotifierInterface):
    def __init__(self):
        self.logger = logging.getLogger('sgae_app')

    def notify_user(self, user_obj) -> bool:
        email = getattr(user_obj, 'email', None)
        first_name = getattr(user_obj, 'first_name', '')
        second_name = getattr(user_obj, 'second_name', '')

        if not email:
            self.logger.error("No se pudo enviar el correo: el usuario no tiene email.")
            return False

        try:
            html_message = render_to_string('account_confirmation.html', {
                'first_name': first_name,
                'second_name': second_name,
            })
            plain_message = strip_tags(html_message)

            send_mail(
                subject='Usuario creado satisfactoriamente',
                message=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                html_message=html_message,
                fail_silently=False
            )

            self.logger.info(f"Correo enviado a {email}")
            return True

        except Exception as e:
            self.logger.error(f"Error al enviar el correo a {email}: {e}")
            return False
