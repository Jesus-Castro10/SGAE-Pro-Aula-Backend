import datetime

class Grade:
    def __init__(self, id: int = None, student=None, subject=None, teacher=None, subperiod: str = None,
                 value: float = 0.0, evaluation_type: str = None,
                 observations: str = None, registered_at: datetime = None):
        if not (0.0 <= value <= 5.0):
            raise ValueError("La nota debe estar entre 0 y 5.")

        self.id = id
        self.student = student
        self.subject = subject
        self.teacher = teacher
        self.subperiod = subperiod
        self.value = round(value, 2)
        self.evaluation_type = evaluation_type
        self.observations = observations
        self.registered_at = registered_at or datetime.now()

    def is_passing(self, passing_grade: float = 3.0):
        return self.value >= passing_grade
