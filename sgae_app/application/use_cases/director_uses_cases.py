from sgae_app.domain.exceptions.exceptions import UserAlreadyExistsException, ResourceNotFoundException
from sgae_app.domain.repositories.director_repository import DirectorRepository
from sgae_app.domain.entities.director import Director
from auth_app.models import User
from sgae_app.domain.utils.mapping import person_mapper

class CreateDirector:
    def __init__(self, repository: DirectorRepository):
        self.repository = repository

    def execute(self, director: Director) -> Director:
        if self.repository.exists(director.email):
            raise UserAlreadyExistsException(f"Director with email {director.email} already exists.")

        user = User.objects.create(
            username=director.email,
            password=director.id_card,
            user_type='director'
        )

        director.user = user
        self.repository.save(director)
        return director


class GetDirector:
    def __init__(self, repository: DirectorRepository):
        self.repository = repository

    def execute(self, director_id: int) -> Director:
        director = self.repository.get_by_id(director_id)
        if not director:
            raise ResourceNotFoundException(f"Director with id {director_id} not found.")
        return director


class UpdateDirector:
    def __init__(self, repository: DirectorRepository):
        self.repository = repository

    def execute(self, director_id: int, update_data: Director) -> Director:
        director_db = self.repository.get_by_id(director_id)
        if not director_db:
            raise ResourceNotFoundException(f"Director with id {director_id} not found.")

        person_mapper(director_db,update_data)
        
        return self.repository.save(director_db)


class DeleteDirector:
    def __init__(self, repository: DirectorRepository):
        self.repository = repository

    def execute(self, director_id: int) -> Director:
        director = self.repository.get_by_id(director_id)
        if not director:
            raise ResourceNotFoundException(f"Director with id {director_id} not found.")

        self.repository.delete(director_id)
        return director


class GetAllDirectors:
    def __init__(self, repository: DirectorRepository):
        self.repository = repository

    def execute(self) -> list[Director]:
        directors = self.repository.get_all()
        if not directors:
            raise ResourceNotFoundException("No directors found.")
        return directors