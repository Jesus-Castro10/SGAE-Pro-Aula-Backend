class StudentDTO:
    def __init__(self, student):
        self.student = student

    def to_dict(self):
        return {
            'id': self.student.id,
            'first_name': self.student.first_name,
            'last_name': self.student.last_name,
            'email': self.student.email
        }