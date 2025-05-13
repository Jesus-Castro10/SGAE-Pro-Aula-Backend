from django.db import models

class TestModel(models.Model):
    def __init__(self, test_id: int, test_name: str):
        self.test_id = test_id
        self.test_name = test_name

    def __repr__(self):
        return f"TestModel(test_id={self.test_id}, test_name='{self.test_name}')"