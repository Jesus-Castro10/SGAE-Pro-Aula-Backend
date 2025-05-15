from auth_app.models import User
from sgae_app.domain.exceptions.exceptions import DuplicateKeyException

class UserService:

    @staticmethod
    def create_user(email: str, id_card: str, user_type: str) -> User:
        if User.objects.filter(username=email).exists():
            raise DuplicateKeyException(f"El usuario con email '{email}' ya existe.")
        
        user = User.objects.create(
            username=email,
            user_type=user_type
        )
        user.set_password(id_card)
        user.save()
        return user
