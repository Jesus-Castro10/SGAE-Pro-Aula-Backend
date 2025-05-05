class DomainException(Exception):
    def __init__(self, message="Error interno del servidor", status_code=500, errors=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.errors = errors

class InvalidDataException(DomainException):
    def __init__(self, errors, message="Datos inválidos", status_code=400):
        formatted_errors = self.format_errors(errors)
        super().__init__(message, status_code)
        self.errors = formatted_errors

    def format_errors(self, errors):
        formatted_errors = []
        for field, messages in errors.items():
            for message in messages:
                if "This field is required" in message:
                    formatted_errors.append(f"The field {field} is required")
        return formatted_errors

class ResourceNotFoundException(DomainException):
    def __init__(self, message="Recurso no encontrado", status_code=404, errors=None):
        super().__init__(message, status_code, errors)

class UserAlreadyExistsException(DomainException):
    def __init__(self, message="Usuario con este email ya existe", status_code=409, errors=None):
        super().__init__(message, status_code, errors)
        
class DuplicateKeyException(DomainException):
    def __init__(self, message="Llave duplicada", status_code=409, errors=None):
        super().__init__(message, status_code, errors)