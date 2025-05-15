from sgae_app.domain.exceptions.exceptions import DuplicateKeyException, ResourceNotFoundException

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
    def __init__(self, repository):
        self.repository = repository

    def execute(self, subject_id: int, subject):
        if not self.repository.get_by_id(subject_id):
            raise ResourceNotFoundException("Subject not found.")
        subject.id = subject_id
        return self.repository.update(subject_id, subject)

class DeleteSubject:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, subject_id: int):
        if not self.repository.get_by_id(subject_id):
            raise ResourceNotFoundException("Subject not found.")
        self.repository.delete_subject(subject_id)
