from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PeriodoAcademicoViewSet,
    DepartamentoViewSet,
    EdificioViewSet,
    PersonaViewSet,
    EstudianteViewSet,
    DocenteViewSet,
    ProgramaViewSet,
    CursoViewSet,
    GrupoCursoViewSet,
    MatriculaViewSet,
    EvaluacionViewSet,
    NotaEvaluacionViewSet,
    AulaViewSet,
    HorarioViewSet,
)

router = DefaultRouter()
# registro de endpoints del api
router.register(r'periodos-academicos',  PeriodoAcademicoViewSet)
router.register(r'departamentos',        DepartamentoViewSet)
router.register(r'edificios',            EdificioViewSet)
router.register(r'personas',             PersonaViewSet)
router.register(r'estudiantes',          EstudianteViewSet)
router.register(r'docentes',             DocenteViewSet)
router.register(r'programas',            ProgramaViewSet)
router.register(r'cursos',               CursoViewSet)
router.register(r'grupos-curso',         GrupoCursoViewSet)
router.register(r'matriculas',           MatriculaViewSet)
router.register(r'evaluaciones',         EvaluacionViewSet)
router.register(r'notas-evaluacion',     NotaEvaluacionViewSet)
router.register(r'aulas',                AulaViewSet)
router.register(r'horarios',             HorarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]