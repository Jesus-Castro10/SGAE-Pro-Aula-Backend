class Schedule:
    def __init__(self, id: int = None):
        self.id = id
        self.items = []  # Optional: List of ScheduleItems

    def add_item(self, item):
        self.items.append(item)

    def total_duration_per_week(self):
        return sum(item.duration_minutes() for item in self.items)
