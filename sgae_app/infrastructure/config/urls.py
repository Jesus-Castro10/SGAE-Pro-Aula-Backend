from django.contrib import admin
from django.urls import path, include

from sgae_app.infrastructure.config.container import Container
from sgae_app.interfaces.api.student_view import StudentView

student_view_instance = Container.student_view()

urlpatterns = [
    path("student/",  student_view_instance.as_view(), name="students"),
]