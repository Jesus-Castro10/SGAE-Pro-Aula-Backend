from sgae_app.domain.exceptions.exceptions import UserAlreadyExistsException

class UserCreatorService:
    def create_user(self, username: str, password: str, user_type: str):
        from auth_app.models import User

        if User.objects.filter(username=username).exists():
            raise UserAlreadyExistsException(f"User with email {username} already exists")
        try:
            user = User.objects.create(
                username=username,
                user_type=user_type
            )
            user.set_password(password)
            user.save()
        except Exception as e:
            raise Exception(f"Error creating user: {str(e)}")
        return user
