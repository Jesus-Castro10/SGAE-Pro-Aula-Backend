from sgae_app.domain.entities.subject import Subject
from sgae_app.application.use_cases.subject_uses_cases import *


class SubjectService:
    def __init__(
        self,
        create_subject_uc: CreateSubject,
        update_subject_uc: UpdateSubject,
        delete_subject_uc: DeleteSubject,
        get_subject_uc: GetSubject,
        get_all_subjects_uc: GetAllSubjects,
    ):
        self.create_subject_uc = create_subject_uc
        self.update_subject_uc = update_subject_uc
        self.delete_subject_uc = delete_subject_uc
        self.get_subject_uc = get_subject_uc
        self.get_all_subjects_uc = get_all_subjects_uc

    def create_subject(self, subject: Subject) -> Subject:
        return self.create_subject_uc.execute(subject)

    def update_subject(self, subject_id: int, subject: Subject) -> Subject:
        return self.update_subject_uc.execute(subject_id, subject)

    def delete_subject(self, subject_id: int) -> Subject:
        return self.delete_subject_uc.execute(subject_id)

    def get_subject(self, subject_id: int) -> Subject:
        return self.get_subject_uc.execute(subject_id)

    def get_all_subjects(self) -> list[Subject]:
        return self.get_all_subjects_uc.execute()
