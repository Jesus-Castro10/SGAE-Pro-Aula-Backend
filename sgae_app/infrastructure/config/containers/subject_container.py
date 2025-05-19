from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djsubject_repository import DjangoSubjectRepository
from sgae_app.application.use_cases.subject_uses_cases import (
    CreateSubject, UpdateSubject, DeleteSubject, GetSubject, GetAllSubjects
)
from sgae_app.application.services.subject_service import SubjectService

class SubjectContainer(containers.DeclarativeContainer):
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
