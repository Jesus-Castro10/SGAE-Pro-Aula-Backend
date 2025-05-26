import datetime
from enum import Enum

class Shift(Enum):
    MAÑANA = "Mañana"
    TARDE = "Tarde"

class Group:
    def __init__(self, id: int = None, name: str = '', year: int = None, section: str = None, shift: Shift = None, schedule=None, registered_at: datetime = None):
        if not name:
            raise ValueError("El nombre del grupo no puede estar vacío.")
        if shift and not isinstance(shift, Shift):
            raise ValueError("El turno debe ser una instancia de Shift")
    

        self.id = id
        self.name = name
        self.year = year
        self.section = section
        self.shift = shift
        self.schedule = schedule
        self.registered_at = registered_at

    def __str__(self):
        """
        Genera una representación legible del grupo.
        
        Ejemplos:
            - "1A - 2025 (Mañana)"
            - "2B - 2025 (Tarde) - Sección A"
        """
        group_str = f"{self.name} - {self.year}"
        if self.shift:
            shift_value = self.shift.value if hasattr(self.shift, 'value') else str(self.shift)
            group_str += f" ({shift_value})"
        if self.section:
            group_str += f" - Sección {self.section}"
        return group_str