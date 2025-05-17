class Schedule:
    def __init__(self, id: int ,code: str, name: str, items: list = None):
        self.id = id
        self.code = code
        self.name = name
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def total_duration_per_week(self):
        return sum(item.duration_minutes() for item in self.items)
