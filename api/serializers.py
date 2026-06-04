from rest_framework import serializers

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

# Serializador para periodo academico
class PeriodoAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoAcademico
        fields = '__all__'

# Serializador para departamento
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

# Serializador para edificio
class EdificioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificio
        fields = '__all__'

# Serializador para persona
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

# Serializador para estudiante
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

# Serializador para docente
class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

# Serializador para programa
class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = '__all__'

# Serializador para curso
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

# Serializador para grupo curso
class GrupoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoCurso
        fields = '__all__'

# Serializador para matricula
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

# Serializador para evaluacion
class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'

# Serializador para nota evaluacion
class NotaEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaEvaluacion
        fields = '__all__'

# Serializador para aula
class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'

# Serializador para horario
class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'