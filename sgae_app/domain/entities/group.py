import datetime

class Group:
    def __init__(self, id: int = None, name: str = '', year: int = None, section: str = None, turn: str = None, schedule=None, registered_at: datetime = None):
        if not name:
            raise ValueError("El nombre del grupo no puede estar vacío.")
    

        self.id = id
        self.name = name
        self.year = year
        self.section = section
        self.turn = turn
        self.schedule = schedule
        self.registered_at = registered_at

    def __str__(self):
        return f"Group(id={self.id}, name={self.name}, year={self.year}, section={self.section}, turn={self.turn}, schedule={self.schedule}, registered_at={self.registered_at})"