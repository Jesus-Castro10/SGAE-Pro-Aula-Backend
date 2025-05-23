from sgae_app.application.services.user_creator_service import UserCreatorService
from sgae_app.application.use_cases.student_uses_cases import *
from sgae_app.domain.entities.student import Student
from sgae_app.interfaces.external.user_notifier_interface import UserNotifierInterface


class StudentService:
    def __init__(self,
                 create_student_uc: CreateStudent,
                 update_student_uc: UpdateStudent,
                 delete_student_uc: DeleteStudent,
                 get_all_students_uc: GetAllStudents,
                 get_student_uc: GetStudent,
                 user_creator: UserCreatorService,
                 user_notifier: UserNotifierInterface):
        
        self.create_student_uc = create_student_uc
        self.update_student_uc = update_student_uc
        self.delete_student_uc = delete_student_uc
        self.get_student_uc = get_student_uc
        self.get_all_students_uc = get_all_students_uc
        self.user_creator = user_creator
        self.user_notifier = user_notifier

    def create_student(self, student: Student):
        student.user = self.user_creator.create_user(student.email, student.id_card, 'student')
        saved = self.create_student_uc.execute(student)
        if saved:
            self.user_notifier.notify_user(student)
        return saved

    def update_student(self, student_id, student: Student):
        return self.update_student_uc.execute(student_id, student)

    def delete_student(self, student_id):
        return self.delete_student_uc.execute(student_id)

    def get_student(self, student_id):
        return self.get_student_uc.execute(student_id)
    
    def get_all_students(self):
        return self.get_all_students_uc.execute()