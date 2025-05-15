from dependency_injector import containers, providers

from sgae_app.application.services.academic_coordi_service import AcademicCoordinatorService
from sgae_app.application.services.director_service import DirectorService
from sgae_app.application.services.secretary_service import SecretaryService
from sgae_app.application.services.subject_service import SubjectService
from sgae_app.application.services.teacher_service import TeacherService
from sgae_app.application.services.student_service import StudentService
from sgae_app.application.services.guardian_service import GuardianService
from sgae_app.application.services.upload_img_service import UploadImgService
from sgae_app.application.services.enrollment_service import EnrollmentService
from sgae_app.application.services.grade_service import GradeService
from sgae_app.application.services.group_service import GroupService
from sgae_app.application.services.classroom_service import ClassRoomService
from sgae_app.application.services.schedule_service import ScheduleService

from sgae_app.infrastructure.repositories.djacademic_coordi_repo import DjangoAcademicCoordinatorRepository
from sgae_app.infrastructure.repositories.djdirector_repository import DjangoDirectorRepository
from sgae_app.infrastructure.repositories.djsecretary_repository import DjangoSecretaryRepository
from sgae_app.infrastructure.repositories.djguardian_repository import DjangoGuardianRepository
from sgae_app.infrastructure.repositories.djstudent_repository import DjangoStudentRepository
from sgae_app.infrastructure.repositories.djteacher_repository import DjangoTeacherRepository
from sgae_app.infrastructure.repositories.djsubject_repository import DjangoSubjectRepository
from sgae_app.infrastructure.repositories.djenrollment_repository import DjangoEnrollmentRepository

from sgae_app.application.use_cases.academic_coordi_uses_cases import *
from sgae_app.application.use_cases.director_uses_cases import *
from sgae_app.application.use_cases.secretary_uses_cases import *
from sgae_app.application.use_cases.student_uses_cases import *
from sgae_app.application.use_cases.guardian_uses_cases import *
from sgae_app.application.use_cases.teacher_uses_cases import *
from sgae_app.application.use_cases.subject_uses_cases import *
from sgae_app.application.use_cases.enrollments_uses_cases import *

from sgae_app.infrastructure.repositories.djgrade_repository import DjangoGradeRepository
from sgae_app.application.use_cases.grade_uses_cases import *
from sgae_app.infrastructure.repositories.djgroup_repository import DjangoGroupRepository
from sgae_app.application.use_cases.group_uses_cases import *
from sgae_app.infrastructure.repositories.djclassroom_repository import DjangoClassRoomRepository
from sgae_app.application.use_cases.classroom_uses_cases import *
from sgae_app.infrastructure.repositories.djschedule_repository import DjangoScheduleRepository
from sgae_app.application.use_cases.schedule_uses_cases import *
from sgae_app.infrastructure.repositories.djschedule_item_repo import DjangoScheduleItemRepository
from sgae_app.application.use_cases.schedule_item_uses_cases import (CreateScheduleItem,
    DeleteScheduleItem, GetAllScheduleItems, GetScheduleItem, UpdateScheduleItem)
from sgae_app.application.services.schedule_item_service import ScheduleItemService

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    # Student Dependencies
    student_repository = providers.Callable(DjangoStudentRepository)

    create_student_use_case = providers.Factory(CreateStudent, repository=student_repository)
    update_student_use_case = providers.Factory(UpdateStudent, repository=student_repository)
    delete_student_use_case = providers.Factory(DeleteStudent, repository=student_repository)
    get_student_use_case = providers.Factory(GetStudent, repository=student_repository)
    get_all_students_use_case = providers.Factory(GetAllStudents, repository=student_repository)

    student_service = providers.Factory(
        StudentService,
        create_student_uc=create_student_use_case,
        update_student_uc=update_student_use_case,
        delete_student_uc=delete_student_use_case,
        get_student_uc=get_student_use_case,
        get_all_students_uc=get_all_students_use_case,
    )

    # Secretary Dependencies
    secretary_repository = providers.Callable(DjangoSecretaryRepository)

    create_secretary_use_case = providers.Factory(CreateSecretary, repository=secretary_repository)
    update_secretary_use_case = providers.Factory(UpdateSecretary, repository=secretary_repository)
    delete_secretary_use_case = providers.Factory(DeleteSecretary, repository=secretary_repository)
    get_secretary_use_case = providers.Factory(GetSecretary, repository=secretary_repository)
    get_all_secretaries_use_case = providers.Factory(GetAllSecretaries, repository=secretary_repository)

    secretary_service = providers.Factory(
        SecretaryService,
        create_secretary_uc=create_secretary_use_case,
        update_secretary_uc=update_secretary_use_case,
        delete_secretary_uc=delete_secretary_use_case,
        get_secretary_uc=get_secretary_use_case,
        get_all_secretaries_uc=get_all_secretaries_use_case,
    )
    
    # Guardian Dependencies
    guardian_repository = providers.Callable(DjangoGuardianRepository)

    create_guardian_use_case = providers.Factory(CreateGuardian, repository=guardian_repository)
    update_guardian_use_case = providers.Factory(UpdateGuardian, repository=guardian_repository)
    delete_guardian_use_case = providers.Factory(DeleteGuardian, repository=guardian_repository)
    get_guardian_use_case = providers.Factory(GetGuardian, repository=guardian_repository)
    get_all_guardians_use_case = providers.Factory(GetAllGuardians, repository=guardian_repository)

    guardian_service = providers.Factory(
        GuardianService,
        create_guardian_uc=create_guardian_use_case,
        update_guardian_uc=update_guardian_use_case,
        delete_guardian_uc=delete_guardian_use_case,
        get_guardian_uc=get_guardian_use_case,
        get_all_guardians_uc=get_all_guardians_use_case,
    )

    #Academic Coordinator Dependencies
    academic_coordinator_repository = providers.Callable(DjangoAcademicCoordinatorRepository)

    create_academic_coordinator_use_case = providers.Factory(CreateAcademicCoordinator, repository=academic_coordinator_repository)
    update_academic_coordinator_use_case = providers.Factory(UpdateAcademicCoordinator, repository=academic_coordinator_repository)
    delete_academic_coordinator_use_case = providers.Factory(DeleteAcademicCoordinator, repository=academic_coordinator_repository)
    get_academic_coordinator_use_case = providers.Factory(GetAcademicCoordinator, repository=academic_coordinator_repository)
    get_all_academic_coordinators_use_case = providers.Factory(GetAllAcademicCoordinators, repository=academic_coordinator_repository)

    academic_coordinator_service = providers.Factory(
        AcademicCoordinatorService,
        create_academic_coordinator_uc=create_academic_coordinator_use_case,
        update_academic_coordinator_uc=update_academic_coordinator_use_case,
        delete_academic_coordinator_uc=delete_academic_coordinator_use_case,
        get_academic_coordinator_uc=get_academic_coordinator_use_case,
        get_all_academic_coordinators_uc=get_all_academic_coordinators_use_case,
    )

    # Director dependencies
    director_repository = providers.Callable(DjangoDirectorRepository)

    create_director_use_case = providers.Factory(CreateDirector, repository=director_repository)
    update_director_use_case = providers.Factory(UpdateDirector, repository=director_repository)
    delete_director_use_case = providers.Factory(DeleteDirector, repository=director_repository)
    get_director_use_case = providers.Factory(GetDirector, repository=director_repository)
    get_all_directors_use_case = providers.Factory(GetAllDirectors, repository=director_repository)

    director_service = providers.Factory(
        DirectorService,
        create_director_uc=create_director_use_case,
        update_director_uc=update_director_use_case,
        delete_director_uc=delete_director_use_case,
        get_director_uc=get_director_use_case,
        get_all_directors_uc=get_all_directors_use_case,
    )

    # Teacher dependencies
    teacher_repository = providers.Callable(DjangoTeacherRepository)

    create_teacher_use_case = providers.Factory(CreateTeacher, repository=teacher_repository)
    update_teacher_use_case = providers.Factory(UpdateTeacher, repository=teacher_repository)
    delete_teacher_use_case = providers.Factory(DeleteTeacher, repository=teacher_repository)
    get_teacher_use_case = providers.Factory(GetTeacher, repository=teacher_repository)
    get_all_teachers_use_case = providers.Factory(GetAllTeachers, repository=teacher_repository)

    teacher_service = providers.Factory(
        TeacherService,
        create_teacher_uc=create_teacher_use_case,
        update_teacher_uc=update_teacher_use_case,
        delete_teacher_uc=delete_teacher_use_case,
        get_teacher_uc=get_teacher_use_case,
        get_all_teachers_uc=get_all_teachers_use_case,
    )
    
    #Subject dependencies
    subject_repository = providers.Callable(DjangoSubjectRepository)

    create_subject_use_case = providers.Factory(CreateSubject, repository=subject_repository)
    update_subject_use_case = providers.Factory(UpdateSubject, repository=subject_repository)
    delete_subject_use_case = providers.Factory(DeleteSubject, repository=subject_repository)
    get_subject_use_case = providers.Factory(GetSubject, repository=subject_repository)
    get_all_subjects_use_case = providers.Factory(GetAllSubjects, repository=subject_repository)

    subject_service = providers.Factory(
        SubjectService,
        create_subject_uc=create_subject_use_case,
        update_subject_uc=update_subject_use_case,
        delete_subject_uc=delete_subject_use_case,
        get_subject_uc=get_subject_use_case,
        get_all_subjects_uc=get_all_subjects_use_case,
    )
    
    #Upload Image dependencies
    upload_img_service = providers.Factory(UploadImgService)
    
    #Enrollment dependencies
    enrollment_repository = providers.Callable(DjangoEnrollmentRepository)

    create_enrollment_use_case = providers.Factory(CreateEnrollment, repository=enrollment_repository)
    update_enrollment_use_case = providers.Factory(UpdateEnrollment, repository=enrollment_repository)
    delete_enrollment_use_case = providers.Factory(DeleteEnrollment, repository=enrollment_repository)
    get_enrollment_use_case = providers.Factory(GetEnrollment, repository=enrollment_repository)
    get_all_enrollments_use_case = providers.Factory(GetAllEnrollments, repository=enrollment_repository)
    get_enrollments_by_student_use_case = providers.Factory(GetEnrollmentsByStudent, repository=enrollment_repository)

    enrollment_service = providers.Factory(
        EnrollmentService,
        create_enrollment_uc=create_enrollment_use_case,
        update_enrollment_uc=update_enrollment_use_case,
        delete_enrollment_uc=delete_enrollment_use_case,
        get_enrollment_uc=get_enrollment_use_case,
        get_all_enrollments_uc=get_all_enrollments_use_case,
        get_enrollments_by_student_uc=get_enrollments_by_student_use_case,
    )

    # Grade dependencies
    grade_repository = providers.Callable(DjangoGradeRepository)

    create_grade_use_case = providers.Factory(CreateGrade, repository=grade_repository)
    update_grade_use_case = providers.Factory(UpdateGrade, repository=grade_repository)
    delete_grade_use_case = providers.Factory(DeleteGrade, repository=grade_repository)
    get_grade_use_case = providers.Factory(GetGrade, repository=grade_repository)
    get_all_grades_use_case = providers.Factory(GetAllGrades, repository=grade_repository)

    grade_service = providers.Factory(
        GradeService,
        create_grade_uc=create_grade_use_case,
        update_grade_uc=update_grade_use_case,
        delete_grade_uc=delete_grade_use_case,
        get_grade_uc=get_grade_use_case,
        get_all_grades_uc=get_all_grades_use_case,
    )

    # Group dependencies
    group_repository = providers.Callable(DjangoGroupRepository)

    create_group_use_case = providers.Factory(CreateGroup, repository=group_repository)
    update_group_use_case = providers.Factory(UpdateGroup, repository=group_repository)
    delete_group_use_case = providers.Factory(DeleteGroup, repository=group_repository)
    get_group_use_case = providers.Factory(GetGroup, repository=group_repository)
    get_all_groups_use_case = providers.Factory(GetAllGroups, repository=group_repository)

    group_service = providers.Factory(
        GroupService,
        create_group_uc=create_group_use_case,
        update_group_uc=update_group_use_case,
        delete_group_uc=delete_group_use_case,
        get_group_uc=get_group_use_case,
        get_all_groups_uc=get_all_groups_use_case,
    )

    # ClassRoom dependencies
    classroom_repository = providers.Callable(DjangoClassRoomRepository)

    create_classroom_use_case = providers.Factory(CreateClassroom, repository=classroom_repository)
    update_classroom_use_case = providers.Factory(UpdateClassroom, repository=classroom_repository)
    delete_classroom_use_case = providers.Factory(DeleteClassroom, repository=classroom_repository)
    get_classroom_use_case = providers.Factory(GetClassroom, repository=classroom_repository)
    get_all_classrooms_use_case = providers.Factory(GetAllClassrooms, repository=classroom_repository)

    classroom_service = providers.Factory(
        ClassRoomService,
        create_classroom_uc=create_classroom_use_case,
        update_classroom_uc=update_classroom_use_case,
        delete_classroom_uc=delete_classroom_use_case,
        get_classroom_uc=get_classroom_use_case,
        get_all_classrooms_uc=get_all_classrooms_use_case,
    )
    
    # Schedule dependencies
    schedule_repository = providers.Callable(DjangoScheduleRepository)

    create_schedule_use_case = providers.Factory(CreateSchedule, repository=schedule_repository)
    update_schedule_use_case = providers.Factory(UpdateSchedule, repository=schedule_repository)
    delete_schedule_use_case = providers.Factory(DeleteSchedule, repository=schedule_repository)
    get_schedule_use_case = providers.Factory(GetSchedule, repository=schedule_repository)
    get_all_schedules_use_case = providers.Factory(GetAllSchedules, repository=schedule_repository)

    schedule_service = providers.Factory(
        ScheduleService,
        create_schedule_uc=create_schedule_use_case,
        update_schedule_uc=update_schedule_use_case,
        delete_schedule_uc=delete_schedule_use_case,
        get_schedule_uc=get_schedule_use_case,
        get_all_schedules_uc=get_all_schedules_use_case,
    )
    
    # ScheduleItem dependencies
    schedule_item_repository = providers.Callable(DjangoScheduleItemRepository)

    create_schedule_item_use_case = providers.Factory(CreateScheduleItem, repository=schedule_item_repository)
    update_schedule_item_use_case = providers.Factory(UpdateScheduleItem, repository=schedule_item_repository)
    delete_schedule_item_use_case = providers.Factory(DeleteScheduleItem, repository=schedule_item_repository)
    get_schedule_item_use_case = providers.Factory(GetScheduleItem, repository=schedule_item_repository)
    get_all_schedule_items_use_case = providers.Factory(GetAllScheduleItems, repository=schedule_item_repository)

    schedule_item_service = providers.Factory(
        ScheduleItemService,
        create_schedule_item_uc=create_schedule_item_use_case,
        update_schedule_item_uc=update_schedule_item_use_case,
        delete_schedule_item_uc=delete_schedule_item_use_case,
        get_schedule_item_uc=get_schedule_item_use_case,
        get_all_schedule_items_uc=get_all_schedule_items_use_case,
    )
