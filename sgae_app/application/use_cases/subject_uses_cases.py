from sgae_app.domain.exceptions.exceptions import ResourceNotFoundException
from sgae_app.domain.repositories.subject_repository import SubjectRepository
from sgae_app.domain.entities.subject import Subject

class CreateSubject:
    def __init__(self, repository: SubjectRepository):
        self.repository = repository

    def execute(self, subject: Subject) -> Subject:
        if self.repository.exists(subject):
            raise ResourceNotFoundException(f"Subject with code {subject.code} already exists.")
        self.repository.save(subject)
        return subject


class GetSubject:
    def __init__(self, repository: SubjectRepository):
        self.repository = repository

    def execute(self, subject_id: int) -> Subject:
        subject = self.repository.get_by_id(subject_id)
        if not subject:
            raise ResourceNotFoundException(f"Subject with id {subject_id} not found.")
        return subject


class UpdateSubject:
    def __init__(self, repository: SubjectRepository):
        self.repository = repository

    def execute(self, subject_id: int, name: str, code: str, description: str = "") -> Subject:
        subject = self.repository.get_by_id(subject_id)
        if not subject:
            raise ResourceNotFoundException(f"Subject with id {subject_id} not found.")

        # subject.name = name
        # subject.code = code
        # subject.description = description
        self.repository.save(subject)
        return subject


class DeleteSubject:
    def __init__(self, repository: SubjectRepository):
        self.repository = repository

    def execute(self, subject_id: int) -> Subject:
        subject = self.repository.get_by_id(subject_id)
        if not subject:
            raise ResourceNotFoundException(f"Subject with id {subject_id} not found.")

        self.repository.delete(subject_id)
        return subject


class GetAllSubjects:
    def __init__(self, repository: SubjectRepository):
        self.repository = repository

    def execute(self) -> list[Subject]:
        subjects = self.repository.get_all()
        if not subjects:
            raise ResourceNotFoundException("No subjects found.")
        return subjects
