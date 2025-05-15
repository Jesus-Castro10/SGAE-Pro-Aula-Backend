from django.urls import path

from sgae_app.interfaces.api.academic_coordinator_view import AcademicCoordinatorView
from sgae_app.interfaces.api.director_view import DirectorView
from sgae_app.interfaces.api.secretary_view import SecretaryView
from sgae_app.interfaces.api.student_view import StudentView
from sgae_app.interfaces.api.guardian_view import GuardianView
from sgae_app.interfaces.api.teacher_view import TeacherView
from sgae_app.interfaces.api.subject_view import SubjectView
from sgae_app.interfaces.api.enrollment_view import EnrollmentView
from sgae_app.interfaces.api.group_view import GroupView
from sgae_app.interfaces.api.schedule_view import ScheduleView
from sgae_app.interfaces.api.schedule_item_view import ScheduleItemView
from sgae_app.interfaces.api.classroom_view import ClassroomView

urlpatterns = [
    path("students/",  StudentView.as_view()),
    path("students/<int:pk>/",  StudentView.as_view()),
    path("secretaries/",  SecretaryView.as_view()),
    path("secretaries/<int:secretary_id>/",  SecretaryView.as_view()),
    path("academics_coordinators/", AcademicCoordinatorView.as_view()),
    path("academics_coordinators/<int:academic_coordinator_id>", AcademicCoordinatorView.as_view()),
    path('directors/', DirectorView.as_view()),
    path('directors/<int:director_id>/', DirectorView.as_view()),
    path('guardians/', GuardianView.as_view()),
    path('guardians/<int:guardian_id>/', GuardianView.as_view()),
    path('teachers/', TeacherView.as_view()),
    path('teachers/<int:pk>/', TeacherView.as_view()),
    path('subjects/', SubjectView.as_view()),
    path('subjects/<int:pk>/', SubjectView.as_view()),
    path('enrollments/', EnrollmentView.as_view()),
    path('enrollments/<int:pk>/', EnrollmentView.as_view()),
    path('groups/', GroupView.as_view()),
    path('groups/<int:pk>/', GroupView.as_view()),
    path('schedules/', ScheduleView.as_view()),
    path('schedules/<int:pk>/', ScheduleView.as_view()),
    path('schedules-items/', ScheduleItemView.as_view()),
    path('schedules-items/<int:pk>/', ScheduleItemView.as_view()),
    path('classrooms/', ClassroomView.as_view()),
    path('classrooms/<int:pk>/', ClassroomView.as_view()),
]