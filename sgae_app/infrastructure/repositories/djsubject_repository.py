from typing import Any

from sgae_app.domain.entities.subject import Subject
from sgae_app.domain.repositories.subject_repository import SubjectRepository
from sgae_app.infrastructure.models.subject import SubjectModel


class DjangoSubjectRepository(SubjectRepository):

    def get_by_id(self, subject_id: int) -> Any | None:
        try:
            model = SubjectModel.objects.get(id=subject_id)
            return model.to_domain()
        except SubjectModel.DoesNotExist:
            return None

    def get_all(self) -> list[Subject]:
        return [model.to_domain() for model in SubjectModel.objects.all()]

    def get_by_code(self, code: str) -> Subject:
        return SubjectModel.objects.filter(code=code).first().to_domain()

    def save(self, subject: Subject) -> Subject:
        model = SubjectModel.from_domain(subject)
        model.save()
        return subject

    def exists(self, subject: Subject) -> bool:
        return SubjectModel.objects.filter(code=subject.code).exists()

    def delete(self, subject_id: int) -> None:
        SubjectModel.objects.filter(id=subject_id).delete()