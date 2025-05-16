from sgae_app.domain.exceptions.exceptions import DuplicateKeyException, ResourceNotFoundException
from sgae_app.domain.entities.subject import Subject
from sgae_app.domain.utils.mapping import mapper as subject_mapper
from sgae_app.infrastructure.repositories.djsubject_repository import DjangoSubjectRepository

class CreateSubject:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, subject):
        if self.repository.exists(subject):
            raise DuplicateKeyException("Subject already exists.")
        return self.repository.save(subject)

class GetSubject:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, subject_id: int):
        subject = self.repository.get_by_id(subject_id)
        if not subject:
            raise ResourceNotFoundException("Subject not found.")
        return subject

class GetAllSubjects:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        subjects = self.repository.get_all()
        if not subjects:
            raise ResourceNotFoundException("No subjects found.")
        return subjects

class UpdateSubject:
    def __init__(self, repository: DjangoSubjectRepository):
        self.repository = repository

    def execute(self, subject_id: int, update_data: Subject):
        subject_db = self.repository.get_by_id(subject_id)
        if not subject_db:
            raise ResourceNotFoundException("Subject not found.")
        subject_mapper(subject_db, update_data, fields=["name","description"])
        print(f"Subject to update: {subject_db}")
        return self.repository.save(subject_db)

class DeleteSubject:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, subject_id: int):
        if not self.repository.get_by_id(subject_id):
            raise ResourceNotFoundException("Subject not found.")
        self.repository.delete(subject_id)
