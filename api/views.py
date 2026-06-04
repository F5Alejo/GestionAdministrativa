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

# crud para periodo academico (GET, POST, PUT, DELETE)
class PeriodoAcademicoViewSet(viewsets.ModelViewSet):
    queryset = PeriodoAcademico.objects.all()
    serializer_class = PeriodoAcademicoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['periodo_id', 'nombre', 'fecha_inicio', 'fecha_fin', 'activo']
    ordering = ['periodo_id']

# crud para departamento
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['departamento_id', 'nombre', 'codigo']
    ordering = ['nombre']

# crud para edificio
class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['edificio_id', 'nombre']
    ordering = ['nombre']

# crud para persona
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['persona_id', 'tipo_doc', 'numero_doc', 'nombres', 'apellidos', 'email', 'activo', 'creado_en']
    ordering = ['apellidos', 'nombres']

# crud para estudiante
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['estudiante_id', 'codigo', 'fecha_ingreso', 'activo']
    ordering = ['codigo']

# crud para docente
class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['docente_id', 'codigo', 'departamento', 'titulo_maximo', 'dedicacion', 'activo']
    ordering = ['codigo']

# crud para programa
class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['programa_id', 'nombre', 'codigo', 'nivel_formacion', 'modalidad', 'activo']
    ordering = ['nombre']

# crud para curso
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['curso_id', 'nombre', 'codigo', 'creditos', 'nivel_semestre', 'electiva', 'activo']
    ordering = ['codigo']

# crud para grupo curso
class GrupoCursoViewSet(viewsets.ModelViewSet):
    queryset = GrupoCurso.objects.all()
    serializer_class = GrupoCursoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['grupo_id', 'curso', 'docente', 'periodo', 'nombre_grupo', 'cupo_maximo', 'modalidad']
    ordering = ['periodo', 'curso', 'nombre_grupo']

# crud para matricula
class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['matricula_id', 'estudiante', 'grupo', 'periodo', 'estado', 'fecha_matricula', 'nota_final']
    ordering = ['-fecha_matricula']

# crud para evaluacion
class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['evaluacion_id', 'grupo', 'tipo', 'nombre', 'fecha_aplicacion', 'porcentaje', 'nota_maxima']
    ordering = ['fecha_aplicacion', 'nombre']

# crud para nota evaluacion
class NotaEvaluacionViewSet(viewsets.ModelViewSet):
    queryset = NotaEvaluacion.objects.all()
    serializer_class = NotaEvaluacionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['nota_id', 'evaluacion', 'estudiante', 'nota', 'ausente', 'registrado_en']
    ordering = ['-registrado_en']

# crud para aula
class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['aula_id', 'edificio', 'tipo', 'nombre', 'piso', 'capacidad', 'activa']
    ordering = ['nombre']

# crud para horario
class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['horario_id', 'grupo', 'aula', 'dia', 'hora_inicio', 'hora_fin']
    ordering = ['dia', 'hora_inicio']