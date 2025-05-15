from typing import List, Optional
from sgae_app.domain.entities.subject_assignament import SubjectAssignment
from sgae_app.domain.repositories.subject_assignment_repo import SubjectAssignmentRepository
from sgae_app.infrastructure.models.subject_assignment import SubjectAssignmentModel

class DjangoSubjectAssignmentRepository(SubjectAssignmentRepository):

    def get_by_id(self, assignment_id: int) -> Optional[SubjectAssignment]:
        try:
            return SubjectAssignmentModel.objects.select_related('teacher', 'subject', 'group', 'classroom').get(id=assignment_id).to_domain()
        except SubjectAssignmentModel.DoesNotExist:
            return None

    def get_all(self) -> List[SubjectAssignment]:
        return [
            m.to_domain()
            for m in SubjectAssignmentModel.objects.select_related('teacher', 'subject', 'group', 'classroom').all()
        ]

    def get_by_teacher(self, teacher_id: int) -> List[SubjectAssignment]:
        return [
            m.to_domain()
            for m in SubjectAssignmentModel.objects.filter(teacher_id=teacher_id).select_related('subject', 'group', 'classroom')
        ]

    def save(self, assignment: SubjectAssignment) -> SubjectAssignment:
        model = SubjectAssignmentModel.from_domain(assignment)
        model.save()
        return model.to_domain()

    def update(self, assignment_id: int, assignment: SubjectAssignment) -> SubjectAssignment:
        existing = SubjectAssignmentModel.objects.get(id=assignment_id)
        updated = SubjectAssignmentModel.from_domain(assignment)
        updated.id = existing.id
        updated.save()
        return updated.to_domain()

    def exists(self, assignment: SubjectAssignment) -> bool:
        return SubjectAssignmentModel.objects.filter(
            teacher=assignment.teacher.id,
            subject=assignment.subject.id,
            group=assignment.group.id,
            academic_year=assignment.academic_year
        ).exists()

    def delete(self, assignment_id: int) -> None:
        SubjectAssignmentModel.objects.filter(id=assignment_id).delete()
