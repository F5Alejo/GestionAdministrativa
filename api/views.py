import json
import logging

from django.utils import timezone
from rest_framework import filters, viewsets

from .models import (
    PeriodoAcademico,
    Departamento,
    Edificio,
    Persona,
    Estudiante,
    Docente,
    Programa,
    Curso,
    GrupoCurso,
    Matricula,
    Evaluacion,
    NotaEvaluacion,
    Aula,
    Horario,
)

from .serializers import (
    PeriodoAcademicoSerializer,
    DepartamentoSerializer,
    EdificioSerializer,
    PersonaSerializer,
    EstudianteSerializer,
    DocenteSerializer,
    ProgramaSerializer,
    CursoSerializer,
    GrupoCursoSerializer,
    MatriculaSerializer,
    EvaluacionSerializer,
    NotaEvaluacionSerializer,
    AulaSerializer,
    HorarioSerializer,
)

audit_logger = logging.getLogger("api.audit")


class AuditLogMixin:

    def perform_create(self, serializer):
        user = self._get_authenticated_user()
        instance = serializer.save(
            usuario_creacion=user,
            usuario_modificacion=user,
        )
        self._write_audit_log("CREO", instance)

    def perform_update(self, serializer):
        instance = serializer.save(usuario_modificacion=self._get_authenticated_user())
        self._write_audit_log("MODIFICO", instance)

    def perform_destroy(self, instance):
        self._write_audit_log("ELIMINO", instance)
        instance.delete()

    def _write_audit_log(self, action, instance):
        request = self.request
        user = getattr(request, "user", None)

        if user and user.is_authenticated:
            username = user.get_username()
            user_id = user.pk
        else:
            username = "anonimo"
            user_id = None

        audit_logger.info(
            json.dumps(
                {
                    "fecha": timezone.now().isoformat(),
                    "accion": action,
                    "usuario_id": user_id,
                    "usuario": username,
                    "ip": self._get_client_ip(request),
                    "metodo": request.method,
                    "ruta": request.get_full_path(),
                    "modelo": instance._meta.label,
                    "tabla": instance._meta.db_table,
                    "registro_id": instance.pk,
                    "registro": str(instance),
                    "campos": list(request.data.keys()) if hasattr(request, "data") else [],
                },
                ensure_ascii=False,
                default=str,
            )
        )

    def _get_client_ip(self, request):
        forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if forwarded_for:
            return forwarded_for.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR")

    def _get_authenticated_user(self):
        user = getattr(self.request, "user", None)
        if user and user.is_authenticated:
            return user
        return None


# crud para periodo academico (GET, POST, PUT, DELETE)
class PeriodoAcademicoViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = PeriodoAcademico.objects.select_related("usuario_creacion", "usuario_modificacion")
    serializer_class = PeriodoAcademicoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['periodo_id', 'nombre', 'fecha_inicio', 'fecha_fin', 'activo']
    ordering = ['periodo_id']

# crud para departamento
class DepartamentoViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Departamento.objects.select_related("usuario_creacion", "usuario_modificacion")
    serializer_class = DepartamentoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['departamento_id', 'nombre', 'codigo']
    ordering = ['nombre']

# crud para edificio
class EdificioViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Edificio.objects.select_related("usuario_creacion", "usuario_modificacion")
    serializer_class = EdificioSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['edificio_id', 'nombre']
    ordering = ['nombre']

# crud para persona
class PersonaViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Persona.objects.select_related("usuario_creacion", "usuario_modificacion")
    serializer_class = PersonaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['persona_id', 'tipo_doc', 'numero_doc', 'nombres', 'apellidos', 'email', 'activo', 'creado_en']
    ordering = ['apellidos', 'nombres']

# crud para estudiante
class EstudianteViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Estudiante.objects.select_related("persona", "usuario_creacion", "usuario_modificacion")
    serializer_class = EstudianteSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['estudiante_id', 'codigo', 'fecha_ingreso', 'activo']
    ordering = ['codigo']

# crud para docente
class DocenteViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Docente.objects.select_related(
        "persona",
        "departamento",
        "usuario_creacion",
        "usuario_modificacion",
    )
    serializer_class = DocenteSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['docente_id', 'codigo', 'departamento', 'titulo_maximo', 'dedicacion', 'activo']
    ordering = ['codigo']

# crud para programa
class ProgramaViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Programa.objects.select_related(
        "departamento",
        "usuario_creacion",
        "usuario_modificacion",
    )
    serializer_class = ProgramaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['programa_id', 'nombre', 'codigo', 'nivel_formacion', 'modalidad', 'activo']
    ordering = ['nombre']

# crud para curso
class CursoViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Curso.objects.select_related(
        "programa",
        "programa__departamento",
        "departamento",
        "usuario_creacion",
        "usuario_modificacion",
    )
    serializer_class = CursoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['curso_id', 'nombre', 'codigo', 'creditos', 'nivel_semestre', 'electiva', 'activo']
    ordering = ['codigo']

# crud para grupo curso
class GrupoCursoViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = GrupoCurso.objects.select_related(
        "curso",
        "curso__programa",
        "curso__programa__departamento",
        "curso__departamento",
        "docente",
        "docente__persona",
        "docente__departamento",
        "periodo",
        "usuario_creacion",
        "usuario_modificacion",
    )
    serializer_class = GrupoCursoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['grupo_id', 'curso', 'docente', 'periodo', 'nombre_grupo', 'cupo_maximo', 'modalidad']
    ordering = ['periodo', 'curso', 'nombre_grupo']

# crud para matricula
class MatriculaViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Matricula.objects.select_related(
        "estudiante",
        "estudiante__persona",
        "grupo",
        "grupo__curso",
        "grupo__curso__programa",
        "grupo__curso__programa__departamento",
        "grupo__curso__departamento",
        "grupo__docente",
        "grupo__docente__persona",
        "grupo__docente__departamento",
        "grupo__periodo",
        "periodo",
        "usuario_creacion",
        "usuario_modificacion",
    )
    serializer_class = MatriculaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['matricula_id', 'estudiante', 'grupo', 'periodo', 'estado', 'fecha_matricula', 'nota_final']
    ordering = ['-fecha_matricula']

# crud para evaluacion
class EvaluacionViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Evaluacion.objects.select_related(
        "grupo",
        "grupo__curso",
        "grupo__curso__programa",
        "grupo__curso__programa__departamento",
        "grupo__curso__departamento",
        "grupo__docente",
        "grupo__docente__persona",
        "grupo__docente__departamento",
        "grupo__periodo",
        "usuario_creacion",
        "usuario_modificacion",
    )
    serializer_class = EvaluacionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['evaluacion_id', 'grupo', 'tipo', 'nombre', 'fecha_aplicacion', 'porcentaje', 'nota_maxima']
    ordering = ['fecha_aplicacion', 'nombre']

# crud para nota evaluacion
class NotaEvaluacionViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = NotaEvaluacion.objects.select_related(
        "evaluacion",
        "evaluacion__grupo",
        "evaluacion__grupo__curso",
        "evaluacion__grupo__curso__programa",
        "evaluacion__grupo__curso__programa__departamento",
        "evaluacion__grupo__curso__departamento",
        "evaluacion__grupo__docente",
        "evaluacion__grupo__docente__persona",
        "evaluacion__grupo__docente__departamento",
        "evaluacion__grupo__periodo",
        "estudiante",
        "estudiante__persona",
        "usuario_creacion",
        "usuario_modificacion",
    )
    serializer_class = NotaEvaluacionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['nota_id', 'evaluacion', 'estudiante', 'nota', 'ausente', 'registrado_en']
    ordering = ['-registrado_en']

# crud para aula
class AulaViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Aula.objects.select_related("edificio", "usuario_creacion", "usuario_modificacion")
    serializer_class = AulaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['aula_id', 'edificio', 'tipo', 'nombre', 'piso', 'capacidad', 'activa']
    ordering = ['nombre']

# crud para horario
class HorarioViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Horario.objects.select_related(
        "grupo",
        "grupo__curso",
        "grupo__curso__programa",
        "grupo__curso__programa__departamento",
        "grupo__curso__departamento",
        "grupo__docente",
        "grupo__docente__persona",
        "grupo__docente__departamento",
        "grupo__periodo",
        "aula",
        "aula__edificio",
        "usuario_creacion",
        "usuario_modificacion",
    )
    serializer_class = HorarioSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['horario_id', 'grupo', 'aula', 'dia', 'hora_inicio', 'hora_fin']
    ordering = ['dia', 'hora_inicio']
