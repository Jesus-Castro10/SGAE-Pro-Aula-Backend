from dependency_injector import containers, providers
from sgae_app.application.services.user_creator_service import UserCreatorService

class UserCreatorContainer(containers.DeclarativeContainer):
    user_creator_service = providers.Factory(UserCreatorService)
