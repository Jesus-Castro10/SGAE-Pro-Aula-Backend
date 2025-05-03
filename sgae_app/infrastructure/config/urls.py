from django.urls import path

from sgae_app.interfaces.api.secretary_view import SecretaryView
from sgae_app.interfaces.api.student_view import StudentView

urlpatterns = [
    path("students/",  StudentView.as_view(), name="students"),
    path("secretaries/",  SecretaryView.as_view(), name="students"),
    path("students/<int:student_id>/",  StudentView.as_view(), name="students_get"),
    path("secretaries/<int:secretary_id>/",  SecretaryView.as_view(), name="secretary_get"),
]