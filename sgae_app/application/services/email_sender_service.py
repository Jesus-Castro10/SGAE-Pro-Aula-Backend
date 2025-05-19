from django.core.mail import send_mail
from django.conf import settings
import logging
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from typing import Dict

logger = logging.getLogger('sgae_app')

class EmailSenderService:
    """
    Service for sending emails related to user accounts.
    Extend this class for more email types as needed.
    """
    @staticmethod
    def send_registration_confirmation_email(user_email: str, first_name: str, second_name: str) -> bool:
        """
        Envía un correo de confirmación de registro al usuario.
        Args:
            user_email (str): Correo del destinatario.
            first_name (str): Primer nombre del usuario.
            second_name (str): Segundo nombre del usuario.
        Returns:
            bool: True si el correo se envió exitosamente, False en caso contrario.
        """
        subject = 'Usuario creado satisfactoriamente'
        context: Dict[str, str] = {
            'first_name': first_name,
            'second_name': second_name,
        }
        try:
            html_message = render_to_string('account_confirmation.html', context)
            plain_message = strip_tags(html_message)
            send_mail(
                subject,
                plain_message,
                settings.EMAIL_HOST_USER,
                [user_email],
                html_message=html_message,
                fail_silently=False,
            )
            logger.info(f"Registration confirmation email successfully sent to {user_email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send registration confirmation email to {user_email}: {e}")
            return False