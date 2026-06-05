from datetime import date

from django.conf import settings
from django.db import models
from django.utils import timezone


class AuditModel(models.Model):
    usuario_creacion = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        editable=False,
        related_name="%(class)s_creados",
    )
    usuario_modificacion = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        editable=False,
        related_name="%(class)s_modificados",
    )

    class Meta:
        abstract = True


# ============================================================
# TABLAS ESENCIALES DEL PROBLEMA (8 entidades + relaciones)
# ============================================================

# modelo tabla periodo academico (necesario: define el contexto de matriculas y grupos)
class PeriodoAcademico(AuditModel):
    periodo_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=False)

    class Meta:
        db_table = "periodos_academicos"
        ordering = ["-fecha_inicio"]

    def __str__(self):
        return self.nombre


# modelo tabla departamento (necesario: lo usan Docente, Programa y Curso)
class Departamento(AuditModel):
    departamento_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120, unique=True)
    codigo = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "departamentos"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


# modelo tabla edificio (necesario: lo usa Aula)
class Edificio(AuditModel):
    edificio_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "edificios"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


# modelo tabla persona (necesario: base de Estudiante y Docente)
class Persona(AuditModel):
    GENEROS = (
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
    )

    persona_id = models.AutoField(primary_key=True)
    tipo_doc = models.CharField(max_length=10)
    numero_doc = models.CharField(max_length=30)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    fecha_nac = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, choices=GENEROS, blank=True, null=True)
    email = models.CharField(max_length=120, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    ciudad = models.CharField(max_length=80, blank=True, null=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(default=timezone.now)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "personas"
        ordering = ["apellidos", "nombres"]
        unique_together = (("tipo_doc", "numero_doc"),)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


# ============================================================
# ENTIDAD 1: ESTUDIANTES
# ============================================================
class Estudiante(AuditModel):
    estudiante_id = models.AutoField(primary_key=True)
    persona = models.OneToOneField(
        Persona,
        models.CASCADE,
        db_column="persona_id",
        related_name="estudiante",
    )
    codigo = models.CharField(max_length=20, unique=True)
    fecha_ingreso = models.DateField(default=date.today)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "estudiantes"
        ordering = ["codigo"]

    def __str__(self):
        return self.codigo


# ============================================================
# ENTIDAD 2: DOCENTES
# ============================================================
class Docente(AuditModel):
    docente_id = models.AutoField(primary_key=True)
    persona = models.OneToOneField(
        Persona,
        models.CASCADE,
        db_column="persona_id",
        related_name="docente",
    )
    codigo = models.CharField(max_length=20, unique=True)
    departamento = models.ForeignKey(
        Departamento,
        models.CASCADE,
        db_column="departamento_id",
        blank=True,
        null=True,
        related_name="docentes",
    )
    titulo_maximo = models.CharField(max_length=100, blank=True, null=True)
    dedicacion = models.CharField(max_length=40, blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "docentes"
        ordering = ["codigo"]

    def __str__(self):
        return self.codigo


# ============================================================
# ENTIDAD 3: PROGRAMAS
# ============================================================
class Programa(AuditModel):
    programa_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=20, unique=True)
    nivel_formacion = models.CharField(max_length=60)
    departamento = models.ForeignKey(
        Departamento,
        models.CASCADE,
        db_column="departamento_id",
        blank=True,
        null=True,
        related_name="programas",
    )
    modalidad = models.CharField(max_length=30, default="Presencial")
    creditos_totales = models.SmallIntegerField(blank=True, null=True)
    duracion_semestres = models.SmallIntegerField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "programas"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


# ============================================================
# ENTIDAD 4: CURSOS  (Relacion: Curso → Programa)
# ============================================================
class Curso(AuditModel):
    curso_id = models.AutoField(primary_key=True)
    programa = models.ForeignKey(
        Programa,
        models.CASCADE,
        db_column="programa_id",
        related_name="cursos",
    )
    departamento = models.ForeignKey(
        Departamento,
        models.CASCADE,
        db_column="departamento_id",
        blank=True,
        null=True,
        related_name="cursos",
    )
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveSmallIntegerField(default=3)
    horas_semana = models.PositiveSmallIntegerField(default=4)
    nivel_semestre = models.SmallIntegerField(blank=True, null=True)
    electiva = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "cursos"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


# modelo tabla grupo curso (necesario: nexo entre Curso, Docente, Periodo y Matricula/Horario)
class GrupoCurso(AuditModel):
    grupo_id = models.AutoField(primary_key=True)
    curso = models.ForeignKey(
        Curso,
        models.CASCADE,
        db_column="curso_id",
        related_name="grupos",
    )
    docente = models.ForeignKey(
        Docente,
        models.CASCADE,
        db_column="docente_id",
        related_name="grupos",
    )
    periodo = models.ForeignKey(
        PeriodoAcademico,
        models.CASCADE,
        db_column="periodo_id",
        related_name="grupos",
    )
    modalidad = models.CharField(max_length=30, default="Presencial")
    nombre_grupo = models.CharField(max_length=10)
    cupo_maximo = models.PositiveSmallIntegerField(default=30)

    class Meta:
        db_table = "grupos_curso"
        ordering = ["periodo", "curso", "nombre_grupo"]
        unique_together = (("curso", "periodo", "nombre_grupo"),)

    def __str__(self):
        return f"{self.curso.codigo} - {self.nombre_grupo}"


# ============================================================
# ENTIDAD 5: MATRÍCULAS  (Relaciones: Matricula → Estudiante, Matricula → Curso vía grupo)
# ============================================================
class Matricula(AuditModel):
    ESTADOS = (
        ("Activa", "Activa"),
        ("Cancelada", "Cancelada"),
        ("Retirada", "Retirada"),
        ("Finalizada", "Finalizada"),
        ("Pendiente pago", "Pendiente pago"),
    )

    matricula_id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante,
        models.CASCADE,
        db_column="estudiante_id",
        related_name="matriculas",
    )
    grupo = models.ForeignKey(
        GrupoCurso,
        models.CASCADE,
        db_column="grupo_id",
        related_name="matriculas",
    )
    periodo = models.ForeignKey(
        PeriodoAcademico,
        models.CASCADE,
        db_column="periodo_id",
        related_name="matriculas",
    )
    estado = models.CharField(max_length=30, choices=ESTADOS, default="Activa")
    fecha_matricula = models.DateTimeField(default=timezone.now)
    nota_final = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "matriculas"
        ordering = ["-fecha_matricula"]
        unique_together = (("estudiante", "grupo"),)

    def __str__(self):
        return f"{self.estudiante_id} - {self.grupo_id}"


# ============================================================
# ENTIDAD 6: EVALUACIONES  (Relaciones: Evaluacion → Curso vía grupo, Evaluacion → Estudiante vía nota)
# ============================================================
class Evaluacion(AuditModel):
    evaluacion_id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(
        GrupoCurso,
        models.CASCADE,
        db_column="grupo_id",
        related_name="evaluaciones",
    )
    tipo = models.CharField(max_length=60)
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    fecha_aplicacion = models.DateField()
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    nota_maxima = models.DecimalField(max_digits=4, decimal_places=2, default=5.00)

    class Meta:
        db_table = "evaluaciones"
        ordering = ["fecha_aplicacion", "nombre"]

    def __str__(self):
        return self.nombre


# modelo tabla nota evaluacion (necesario: implementa la relacion Evaluacion → Estudiante)
class NotaEvaluacion(AuditModel):
    nota_id = models.AutoField(primary_key=True)
    evaluacion = models.ForeignKey(
        Evaluacion,
        models.CASCADE,
        db_column="evaluacion_id",
        related_name="notas",
    )
    estudiante = models.ForeignKey(
        Estudiante,
        models.CASCADE,
        db_column="estudiante_id",
        related_name="notas_evaluacion",
    )
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ausente = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)
    registrado_en = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "notas_evaluacion"
        ordering = ["-registrado_en"]
        unique_together = (("evaluacion", "estudiante"),)

    def __str__(self):
        return f"{self.evaluacion_id} - {self.estudiante_id}"


# ============================================================
# ENTIDAD 7: AULAS  (necesario para la relacion Horario → Aula)
# ============================================================
class Aula(AuditModel):
    aula_id = models.AutoField(primary_key=True)
    edificio = models.ForeignKey(
        Edificio,
        models.CASCADE,
        db_column="edificio_id",
        blank=True,
        null=True,
        related_name="aulas",
    )
    tipo = models.CharField(max_length=60, default="Salon de clase")
    nombre = models.CharField(max_length=30)
    piso = models.SmallIntegerField(blank=True, null=True)
    capacidad = models.PositiveSmallIntegerField()
    activa = models.BooleanField(default=True)

    class Meta:
        db_table = "aulas"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


# ============================================================
# ENTIDAD 8: HORARIOS  (Relaciones: Horario → Curso vía grupo, Horario → Aula)
# ============================================================
class Horario(AuditModel):
    DIAS = (
        ("Lunes", "Lunes"),
        ("Martes", "Martes"),
        ("Miércoles", "Miércoles"),
        ("Jueves", "Jueves"),
        ("Viernes", "Viernes"),
        ("Sábado", "Sábado"),
        ("Domingo", "Domingo"),
    )

    horario_id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(
        GrupoCurso,
        models.CASCADE,
        db_column="grupo_id",
        related_name="horarios",
    )
    aula = models.ForeignKey(
        Aula,
        models.CASCADE,
        db_column="aula_id",
        related_name="horarios",
    )
    dia = models.CharField(max_length=12, choices=DIAS)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        db_table = "horarios"
        ordering = ["dia", "hora_inicio"]
        unique_together = (("aula", "dia", "hora_inicio"),)

    def __str__(self):
        return f"{self.dia} {self.hora_inicio}-{self.hora_fin}"
