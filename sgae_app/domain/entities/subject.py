class Subject:
    def __init__(self, name: str, code: str, description: str):
        self.description = description
        self.name = name
        self.code = code

    def __str__(self):
        return f"Subject(name={self.name}, code={self.code})"

    def __repr__(self):
        return self.__str__()