from dependency_injector import containers, providers

from sgae_app.application.services.academic_coordi_service import AcademicCoordinatorService
from sgae_app.application.services.director_service import DirectorService
from sgae_app.application.services.secretary_service import SecretaryService
from sgae_app.application.services.subject_service import SubjectService
from sgae_app.application.services.teacher_service import TeacherService
from sgae_app.application.services.student_service import StudentService
from sgae_app.application.services.guardian_service import GuardianService
from sgae_app.application.services.upload_img_service import UploadImgService

from sgae_app.infrastructure.repositories.djacademic_coordi_repo import DjangoAcademicCoordinatorRepository
from sgae_app.infrastructure.repositories.djdirector_repository import DjangoDirectorRepository
from sgae_app.infrastructure.repositories.djsecretary_repository import DjangoSecretaryRepository
from sgae_app.infrastructure.repositories.djguardian_repository import DjangoGuardianRepository
from sgae_app.infrastructure.repositories.djstudent_repository import DjangoStudentRepository
from sgae_app.infrastructure.repositories.djteacher_repository import DjangoTeacherRepository
from sgae_app.infrastructure.repositories.djsubject_repository import DjangoSubjectRepository

from sgae_app.application.use_cases.academic_coordi_uses_cases import *
from sgae_app.application.use_cases.director_uses_cases import *
from sgae_app.application.use_cases.secretary_uses_cases import *
from sgae_app.application.use_cases.student_uses_cases import *
from sgae_app.application.use_cases.guardian_uses_cases import *
from sgae_app.application.use_cases.teacher_uses_cases import *
from sgae_app.application.use_cases.subject_uses_cases import *

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