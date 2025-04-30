from django.urls import path

from sgae_app.interfaces.api.student_view import StudentView

urlpatterns = [
    path("student/",  StudentView.as_view(), name="students"),
    path("student/<int:student_id>/",  StudentView.as_view(), name="students_get"),
]