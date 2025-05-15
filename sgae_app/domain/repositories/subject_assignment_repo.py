from sgae_app.domain.entities.subject_assignament import SubjectAssignment

class SubjectAssignmentRepository:
    def get_all(self) -> list[SubjectAssignment]:
        raise NotImplementedError

    def get_by_id(self, assignment_id: int) -> SubjectAssignment:
        raise NotImplementedError

    def get_by_teacher(self, teacher_id: int) -> list[SubjectAssignment]:
        raise NotImplementedError

    def save(self, assignment: SubjectAssignment) -> SubjectAssignment:
        raise NotImplementedError

    def update(self, assignment_id: int, assignment: SubjectAssignment) -> SubjectAssignment:
        raise NotImplementedError

    def exists(self, assignment: SubjectAssignment) -> bool:
        raise NotImplementedError

    def delete(self, assignment_id: int) -> None:
        raise NotImplementedError
