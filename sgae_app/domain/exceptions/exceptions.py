class DomainException(Exception):
    def __init__(self, message= "Error interno de servidor"):
        super().__init__(message)
        self.message = message

class InvalidDataException(DomainException):
    def __init__(self, message="Datos inválidos"):
        super().__init__(message)
        self.message = message
        
class ResourceNotFoundException(DomainException):
    def __init__(self, message="Recurso no encontrado"):
        super().__init__(message)
        self.message = message