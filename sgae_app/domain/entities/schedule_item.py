from datetime import date, time, datetime

class ScheduleItem:
    VALID_DAYS = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}

    def __init__(self, id: int = None, schedule=None, subject_assignment=None, day_of_week: str = '', start_time: time = None, end_time: time = None):
        if day_of_week not in self.VALID_DAYS:
            raise ValueError(f"Día de la semana inválido: {day_of_week}")
        if start_time >= end_time:
            raise ValueError("La hora de inicio debe ser anterior a la de fin.")

        self.id = id
        self.schedule = schedule
        self.subject_assignment = subject_assignment
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time

    def duration_minutes(self):
        return (datetime.combine(date.today(), self.end_time) - datetime.combine(date.today(), self.start_time)).seconds // 60
