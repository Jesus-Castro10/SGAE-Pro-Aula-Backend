from django.urls import path

from sgae_app.interfaces.api.academic_coordinator_view import AcademicCoordinatorView
from sgae_app.interfaces.api.director_view import DirectorView
from sgae_app.interfaces.api.secretary_view import SecretaryView
from sgae_app.interfaces.api.student_view import StudentView
from sgae_app.interfaces.api.guardian_view import GuardianView
from sgae_app.interfaces.api.teacher_view import TeacherView
from sgae_app.interfaces.api.subject_view import SubjectView

urlpatterns = [
    path("students/",  StudentView.as_view(), name="students"),
    path("students/<int:pk>/",  StudentView.as_view(), name="students_get"),
    path("secretaries/",  SecretaryView.as_view(), name="students"),
    path("secretaries/<int:secretary_id>/",  SecretaryView.as_view(), name="secretary_get"),
    path("academics_coordinators/", AcademicCoordinatorView.as_view(), name="academic_coordinators"),
    path("academics_coordinators/<int:academic_coordinator_id>", AcademicCoordinatorView.as_view(), name="academic_coordinators_get"),
    path('directors/', DirectorView.as_view()),
    path('directors/<int:director_id>/', DirectorView.as_view()),
    path('guardians/', GuardianView.as_view()),
    path('guardians/<int:guardian_id>/', GuardianView.as_view()),
    path('teachers/', TeacherView.as_view()),
    path('teachers/<int:pk>/', TeacherView.as_view()),
    path('subjects/', SubjectView.as_view()),
    path('subjects/<int:pk>/', SubjectView.as_view())
]