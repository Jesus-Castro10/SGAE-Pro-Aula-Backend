from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djgrade_repository import DjangoGradeRepository
from sgae_app.application.use_cases.grade_uses_cases import (
    CreateGrade, UpdateGrade, DeleteGrade, GetGrade, GetAllGrades
)
from sgae_app.application.services.grade_service import GradeService

class GradeContainer(containers.DeclarativeContainer):
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
