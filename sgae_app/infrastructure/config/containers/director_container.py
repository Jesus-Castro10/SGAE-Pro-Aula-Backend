from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djdirector_repository import DjangoDirectorRepository
from sgae_app.application.use_cases.director_uses_cases import (
    CreateDirector, UpdateDirector, DeleteDirector, GetDirector, GetAllDirectors
)
from sgae_app.application.services.director_service import DirectorService
from sgae_app.infrastructure.config.containers.user_creator_container import UserCreatorContainer

class DirectorContainer(containers.DeclarativeContainer):
    user_creator_container = providers.Container(UserCreatorContainer)

    director_repository = providers.Callable(DjangoDirectorRepository)

    create_director_use_case = providers.Factory(CreateDirector, repository=director_repository)
    update_director_use_case = providers.Factory(UpdateDirector, repository=director_repository)
    delete_director_use_case = providers.Factory(DeleteDirector, repository=director_repository)
    get_director_use_case = providers.Factory(GetDirector, repository=director_repository)
    get_all_directors_use_case = providers.Factory(GetAllDirectors, repository=director_repository)

    director_service = providers.Factory(
        DirectorService,
        create_director_uc=create_director_use_case,
        update_director_uc=update_director_use_case,
        delete_director_uc=delete_director_use_case,
        get_director_uc=get_director_use_case,
        get_all_directors_uc=get_all_directors_use_case,
        user_creator=user_creator_container.user_creator_service,
    )
