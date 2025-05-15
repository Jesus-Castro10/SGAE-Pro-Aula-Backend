from sgae_app.domain.exceptions.exceptions import DuplicateKeyException, ResourceNotFoundException

class CreateGrade:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, grade):
        if self.repository.exists(grade):
            raise DuplicateKeyException("Grade already exists.")
        return self.repository.save(grade)

class GetGrade:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, grade_id: int):
        grade = self.repository.get_by_id(grade_id)
        if not grade:
            raise ResourceNotFoundException("Grade not found.")
        return grade

class GetAllGrades:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        grades = self.repository.get_all()
        if not grades:
            raise ResourceNotFoundException("No grades found.")
        return grades

class UpdateGrade:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, grade_id: int, grade):
        if not self.repository.get_by_id(grade_id):
            raise ResourceNotFoundException("Grade not found.")
        grade.id = grade_id
        return self.repository.update(grade_id, grade)

class DeleteGrade:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, grade_id: int):
        if not self.repository.get_by_id(grade_id):
            raise ResourceNotFoundException("Grade not found.")
        self.repository.delete(grade_id)
