import datetime

class Group:
    def __init__(self, id: int = None, name: str = '', year: int = None, section: str = None, shift: str = None, schedule=None, registered_at: datetime = None):
        if not name:
            raise ValueError("El nombre del grupo no puede estar vacío.")
        if year < 2000:
            raise ValueError("El año del grupo debe ser válido.")

        self.id = id
        self.name = name
        self.year = year
        self.section = section
        self.shift = shift
        self.schedule = schedule
        self.registered_at = registered_at
