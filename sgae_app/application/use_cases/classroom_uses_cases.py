from sgae_app.domain.exceptions.exceptions import DuplicateKeyException, ResourceNotFoundException


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
        if not self.repository.get_by_id(classroom_id):
            raise ResourceNotFoundException("Classroom not found.")
        classroom.id = classroom_id
        return self.repository.update(classroom_id, classroom)

class DeleteClassroom:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, classroom_id: int):
        if not self.repository.get_by_id(classroom_id):
            raise ResourceNotFoundException("Classroom not found.")
        self.repository.delete(classroom_id)
