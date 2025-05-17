from sgae_app.domain.exceptions.exceptions import DuplicateKeyException, ResourceNotFoundException
from sgae_app.domain.utils.mapping import mapper as classroom_mapper

class CreateClassroom:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, classroom):
        if self.repository.exists(classroom):
            raise DuplicateKeyException("Classroom already exists.")
        return self.repository.save(classroom)

class GetClassroom:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, classroom_id: int):
        classroom = self.repository.get_by_id(classroom_id)
        if not classroom:
            raise ResourceNotFoundException("Classroom not found.")
        return classroom

class GetAllClassrooms:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        classrooms = self.repository.get_all()
        if not classrooms:
            raise ResourceNotFoundException("No classrooms found.")
        return classrooms

class UpdateClassroom:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, classroom_id: int, classroom):
        classroom_db = self.repository.get_by_id(classroom_id)
        if not classroom_db:
            raise ResourceNotFoundException("Classroom not found.")
        
        classroom_mapper(classroom_db, classroom, fields=["name", "capacity", "registered_at"])
        return self.repository.save(classroom_db)

class DeleteClassroom:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, classroom_id: int):
        if not self.repository.get_by_id(classroom_id):
            raise ResourceNotFoundException("Classroom not found.")
        self.repository.delete(classroom_id)
