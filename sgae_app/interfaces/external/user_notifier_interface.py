from abc import ABC, abstractmethod

class UserNotifierInterface(ABC):
    @abstractmethod
    def notify_user(self, user_obj) -> bool:
        """
        Envía una notificación al usuario, por ejemplo, un correo de bienvenida.
        :param user_obj: Objeto con los datos del usuario.
        :return: True si se envió exitosamente, False si falló.
        """
        pass
