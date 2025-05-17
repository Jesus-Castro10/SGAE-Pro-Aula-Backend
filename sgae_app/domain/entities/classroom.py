from datetime import datetime

class Classroom:
    def __init__(self, id: int = None, name: str = '', capacity: int = 0, registered_at: datetime = None):
        if not name:
            raise ValueError("El nombre del aula no puede estar vacío.")
        if capacity <= 0:
            raise ValueError("La capacidad debe ser mayor a cero.")

        self.id = id
        self.name = name
        self.capacity = capacity
        self.registered_at = registered_at

    def __str__(self):
        return f"Aula(id={self.id}, name='{self.name}', capacity={self.capacity}, registered_at={self.registered_at})"
