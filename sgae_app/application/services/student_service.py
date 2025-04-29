from sgae_app.domain.use_cases.student import CreateStudent, UpdateStudent, DeleteStudent, GetStudent


class StudentService:
    def __init__(self,
                 create_student_uc: CreateStudent,
                 update_student_uc: UpdateStudent,
                 delete_student_uc: DeleteStudent,
                 get_student_uc: GetStudent):
        self.create_student_uc = create_student_uc
        self.update_student_uc = update_student_uc
        self.delete_student_uc = delete_student_uc
        self.get_student_uc = get_student_uc

    def create_student(self, first_name, second_name, first_lastname, second_lastname, id_card, birthdate, place_of_birth, address, phone, email):
        return self.create_student_uc.execute(
            first_name=first_name,
            second_name=second_name,
            first_lastname=first_lastname,
            second_lastname=second_lastname,
            id_card=id_card,
            birthdate=birthdate,
            place_of_birth=place_of_birth,
            address=address,
            phone=phone,
            email=email
        )

    def update_student(self, student_id, first_name, last_name, email):
        return self.update_student_uc.execute(student_id, first_name, last_name, email)

    def delete_student(self, student_id):
        return self.delete_student_uc.execute(student_id)

    def get_student(self, student_id):
        return self.get_student_uc.execute(student_id)