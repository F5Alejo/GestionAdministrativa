from rest_framework import serializers
from django.contrib.auth import get_user_model

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

User = get_user_model()


class UsuarioSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "is_staff")


class AuditSerializerMixin(serializers.ModelSerializer):
    usuario_creacion_detalle = UsuarioSimpleSerializer(
        source="usuario_creacion",
        read_only=True,
    )
    usuario_modificacion_detalle = UsuarioSimpleSerializer(
        source="usuario_modificacion",
        read_only=True,
    )


class PeriodoAcademicoResumenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoAcademico
        fields = ("periodo_id", "nombre", "fecha_inicio", "fecha_fin", "activo")


class DepartamentoResumenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ("departamento_id", "nombre", "codigo")


class EdificioResumenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificio
        fields = ("edificio_id", "nombre", "direccion")


class PersonaResumenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ("persona_id", "tipo_doc", "numero_doc", "nombres", "apellidos", "email")


class EstudianteResumenSerializer(serializers.ModelSerializer):
    persona_detalle = PersonaResumenSerializer(source="persona", read_only=True)

    class Meta:
        model = Estudiante
        fields = ("estudiante_id", "codigo", "persona", "persona_detalle", "activo")


class DocenteResumenSerializer(serializers.ModelSerializer):
    persona_detalle = PersonaResumenSerializer(source="persona", read_only=True)
    departamento_detalle = DepartamentoResumenSerializer(source="departamento", read_only=True)

    class Meta:
        model = Docente
        fields = (
            "docente_id",
            "codigo",
            "persona",
            "persona_detalle",
            "departamento",
            "departamento_detalle",
            "activo",
        )


class ProgramaResumenSerializer(serializers.ModelSerializer):
    departamento_detalle = DepartamentoResumenSerializer(source="departamento", read_only=True)

    class Meta:
        model = Programa
        fields = (
            "programa_id",
            "nombre",
            "codigo",
            "departamento",
            "departamento_detalle",
            "activo",
        )


class CursoResumenSerializer(serializers.ModelSerializer):
    programa_detalle = ProgramaResumenSerializer(source="programa", read_only=True)
    departamento_detalle = DepartamentoResumenSerializer(source="departamento", read_only=True)

    class Meta:
        model = Curso
        fields = (
            "curso_id",
            "nombre",
            "codigo",
            "programa",
            "programa_detalle",
            "departamento",
            "departamento_detalle",
            "activo",
        )


class GrupoCursoResumenSerializer(serializers.ModelSerializer):
    curso_detalle = CursoResumenSerializer(source="curso", read_only=True)
    docente_detalle = DocenteResumenSerializer(source="docente", read_only=True)
    periodo_detalle = PeriodoAcademicoResumenSerializer(source="periodo", read_only=True)

    class Meta:
        model = GrupoCurso
        fields = (
            "grupo_id",
            "curso",
            "curso_detalle",
            "docente",
            "docente_detalle",
            "periodo",
            "periodo_detalle",
            "nombre_grupo",
            "modalidad",
            "cupo_maximo",
        )


class EvaluacionResumenSerializer(serializers.ModelSerializer):
    grupo_detalle = GrupoCursoResumenSerializer(source="grupo", read_only=True)

    class Meta:
        model = Evaluacion
        fields = ("evaluacion_id", "grupo", "grupo_detalle", "tipo", "nombre")


class AulaResumenSerializer(serializers.ModelSerializer):
    edificio_detalle = EdificioResumenSerializer(source="edificio", read_only=True)

    class Meta:
        model = Aula
        fields = ("aula_id", "edificio", "edificio_detalle", "tipo", "nombre", "capacidad", "activa")


# Serializador para periodo academico
class PeriodoAcademicoSerializer(AuditSerializerMixin):
    class Meta:
        model = PeriodoAcademico
        fields = '__all__'

# Serializador para departamento
class DepartamentoSerializer(AuditSerializerMixin):
    class Meta:
        model = Departamento
        fields = '__all__'

# Serializador para edificio
class EdificioSerializer(AuditSerializerMixin):
    class Meta:
        model = Edificio
        fields = '__all__'

# Serializador para persona
class PersonaSerializer(AuditSerializerMixin):
    class Meta:
        model = Persona
        fields = '__all__'

# Serializador para estudiante
class EstudianteSerializer(AuditSerializerMixin):
    persona_detalle = PersonaResumenSerializer(source="persona", read_only=True)

    class Meta:
        model = Estudiante
        fields = '__all__'

# Serializador para docente
class DocenteSerializer(AuditSerializerMixin):
    persona_detalle = PersonaResumenSerializer(source="persona", read_only=True)
    departamento_detalle = DepartamentoResumenSerializer(source="departamento", read_only=True)

    class Meta:
        model = Docente
        fields = '__all__'

# Serializador para programa
class ProgramaSerializer(AuditSerializerMixin):
    departamento_detalle = DepartamentoResumenSerializer(source="departamento", read_only=True)

    class Meta:
        model = Programa
        fields = '__all__'

# Serializador para curso
class CursoSerializer(AuditSerializerMixin):
    programa_detalle = ProgramaResumenSerializer(source="programa", read_only=True)
    departamento_detalle = DepartamentoResumenSerializer(source="departamento", read_only=True)

    class Meta:
        model = Curso
        fields = '__all__'

# Serializador para grupo curso
class GrupoCursoSerializer(AuditSerializerMixin):
    curso_detalle = CursoResumenSerializer(source="curso", read_only=True)
    docente_detalle = DocenteResumenSerializer(source="docente", read_only=True)
    periodo_detalle = PeriodoAcademicoResumenSerializer(source="periodo", read_only=True)

    class Meta:
        model = GrupoCurso
        fields = '__all__'

# Serializador para matricula
class MatriculaSerializer(AuditSerializerMixin):
    estudiante_detalle = EstudianteResumenSerializer(source="estudiante", read_only=True)
    grupo_detalle = GrupoCursoResumenSerializer(source="grupo", read_only=True)
    periodo_detalle = PeriodoAcademicoResumenSerializer(source="periodo", read_only=True)

    class Meta:
        model = Matricula
        fields = '__all__'

# Serializador para evaluacion
class EvaluacionSerializer(AuditSerializerMixin):
    grupo_detalle = GrupoCursoResumenSerializer(source="grupo", read_only=True)

    class Meta:
        model = Evaluacion
        fields = '__all__'

# Serializador para nota evaluacion
class NotaEvaluacionSerializer(AuditSerializerMixin):
    evaluacion_detalle = EvaluacionResumenSerializer(source="evaluacion", read_only=True)
    estudiante_detalle = EstudianteResumenSerializer(source="estudiante", read_only=True)

    class Meta:
        model = NotaEvaluacion
        fields = '__all__'

# Serializador para aula
class AulaSerializer(AuditSerializerMixin):
    edificio_detalle = EdificioResumenSerializer(source="edificio", read_only=True)

    class Meta:
        model = Aula
        fields = '__all__'

# Serializador para horario
class HorarioSerializer(AuditSerializerMixin):
    grupo_detalle = GrupoCursoResumenSerializer(source="grupo", read_only=True)
    aula_detalle = AulaResumenSerializer(source="aula", read_only=True)

    class Meta:
        model = Horario
        fields = '__all__'
