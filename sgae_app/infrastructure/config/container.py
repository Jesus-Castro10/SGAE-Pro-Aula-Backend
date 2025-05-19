from dependency_injector import containers, providers

from sgae_app.infrastructure.config.containers.student_container import StudentContainer
from sgae_app.infrastructure.config.containers.teacher_container import TeacherContainer
from sgae_app.infrastructure.config.containers.guardian_container import GuardianContainer
from sgae_app.infrastructure.config.containers.secretary_container import SecretaryContainer
from sgae_app.infrastructure.config.containers.director_container import DirectorContainer
from sgae_app.infrastructure.config.containers.academic_coor_container import AcademicCoordinatorContainer
from sgae_app.infrastructure.config.containers.subject_container import SubjectContainer
from sgae_app.infrastructure.config.containers.enrollment_container import EnrollmentContainer
from sgae_app.infrastructure.config.containers.classroom_container import ClassroomContainer
from sgae_app.infrastructure.config.containers.schedule_container import ScheduleContainer
from sgae_app.infrastructure.config.containers.grade_container import GradeContainer
from sgae_app.infrastructure.config.containers.group_container import GroupContainer
from sgae_app.infrastructure.config.containers.schedule_item_container import ScheduleItemContainer
from sgae_app.infrastructure.config.containers.email_container import EmailContainer
from sgae_app.infrastructure.config.containers.user_creator_container import UserCreatorContainer

class Container(containers.DeclarativeContainer):
    #config = containers.WiringConfiguration(packages=["sgae_app.interfaces.api"])

    config = providers.Configuration()
    
    user_creator = providers.Container(UserCreatorContainer)
    email = providers.Container(EmailContainer)

    student = providers.Container(StudentContainer)
    teacher = providers.Container(TeacherContainer)
    guardian = providers.Container(GuardianContainer)
    secretary = providers.Container(SecretaryContainer)
    director = providers.Container(DirectorContainer)
    academic_coordinator = providers.Container(AcademicCoordinatorContainer)
    subject = providers.Container(SubjectContainer)
    enrollment = providers.Container(EnrollmentContainer)
    classroom = providers.Container(ClassroomContainer)
    schedule = providers.Container(ScheduleContainer)
    grade = providers.Container(GradeContainer)
    group = providers.Container(GroupContainer)
    schedule_item = providers.Container(ScheduleItemContainer)
