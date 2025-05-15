from sgae_app.application.use_cases.grade_uses_cases import *
from sgae_app.domain.entities.grade import Grade

class GradeService:
    def __init__(self,
                 create_grade_uc: CreateGrade,
                 update_grade_uc: UpdateGrade,
                 delete_grade_uc: DeleteGrade,
                 get_grade_uc: GetGrade,
                 get_all_grades_uc: GetAllGrades):
        
        self.create_grade_uc = create_grade_uc
        self.update_grade_uc = update_grade_uc
        self.delete_grade_uc = delete_grade_uc
        self.get_grade_uc = get_grade_uc
        self.get_all_grades_uc = get_all_grades_uc

    def create(self, grade: Grade):
        return self.create_grade_uc.execute(grade)

    def update(self, grade_id, grade: Grade):
        return self.update_grade_uc.execute(grade_id, grade)

    def delete(self, grade_id):
        return self.delete_grade_uc.execute(grade_id)

    def get(self, grade_id):
        return self.get_grade_uc.execute(grade_id)

    def get_all(self):
        return self.get_all_grades_uc.execute()
