from django.db import migrations


def create_initial_data(apps, schema_editor):
    PeriodoAcademico = apps.get_model('api', 'PeriodoAcademico')
    Departamento = apps.get_model('api', 'Departamento')
    Persona = apps.get_model('api', 'Persona')
    Estudiante = apps.get_model('api', 'Estudiante')
    Docente = apps.get_model('api', 'Docente')
    Programa = apps.get_model('api', 'Programa')
    Curso = apps.get_model('api', 'Curso')
    GrupoCurso = apps.get_model('api', 'GrupoCurso')
    Usuario = apps.get_model('api', 'Usuario')
    
    periodo, _ = PeriodoAcademico.objects.get_or_create(
        nombre='2026 - II',
        defaults={
            'fecha_inicio': '2026-08-01',
            'fecha_fin': '2026-12-15',
            'activo': True,
        },
    )

    departamento, _ = Departamento.objects.get_or_create(
        codigo='INF',
        defaults={'nombre': 'Ingeniería Informática'},
    )

    persona_est, _ = Persona.objects.get_or_create(
        tipo_doc='CC',
        numero_doc='10000001',
        defaults={
            'nombres': 'Carlos',
            'apellidos': 'Pérez',
            'fecha_nac': '2002-05-10',
            'genero': 'M',
            'email': 'carlos.perez@example.com',
            'telefono': '3001234567',
            'direccion': 'Calle 123',
            'ciudad': 'Medellín',
            'activo': True,
        },
    )

    estudiante, _ = Estudiante.objects.get_or_create(
        persona=persona_est,
        defaults={
            'codigo': 'ESTU-0001',
            'fecha_ingreso': '2024-01-15',
            'activo': True,
        },
    )

    persona_doc, _ = Persona.objects.get_or_create(
        tipo_doc='CC',
        numero_doc='10000002',
        defaults={
            'nombres': 'María',
            'apellidos': 'González',
            'fecha_nac': '1985-03-22',
            'genero': 'F',
            'email': 'maria.gonzalez@example.com',
            'telefono': '3107654321',
            'direccion': 'Carrera 45',
            'ciudad': 'Bogotá',
            'activo': True,
        },
    )

    docente, _ = Docente.objects.get_or_create(
        persona=persona_doc,
        defaults={
            'codigo': 'DOC-001',
            'departamento': departamento,
            'titulo_maximo': 'Magíster en Ciencias de la Computación',
            'dedicacion': 'Tiempo completo',
            'rol': 'Profesor',
            'fecha_vinculacion': '2020-02-01',
            'activo': True,
        },
    )

    programa, _ = Programa.objects.get_or_create(
        codigo='INF-2026',
        defaults={
            'nombre': 'Ingeniería Informática',
            'nivel_formacion': 'Pregrado',
            'departamento': departamento,
            'director': docente,
            'modalidad': 'Presencial',
            'creditos_totales': 160,
            'duracion_semestres': 10,
            'activo': True,
            'descripcion': 'Programa de formación en ingeniería de software y sistemas de información.',
        },
    )

    curso, _ = Curso.objects.get_or_create(
        codigo='INF101',
        defaults={
            'programa': programa,
            'departamento': departamento,
            'nombre': 'Fundamentos de Programación',
            'creditos': 4,
            'horas_semana': 4,
            'nivel_semestre': 1,
            'electiva': False,
            'activo': True,
            'descripcion': 'Curso introductorio de programación con Python.',
        },
    )

    GrupoCurso.objects.get_or_create(
        curso=curso,
        periodo=periodo,
        nombre_grupo='A',
        defaults={
            'docente': docente,
            'modalidad': 'Presencial',
            'cupo_maximo': 30,
        },
    )

    Usuario.objects.get_or_create(
        username='admin',
        defaults={
            'persona': persona_doc,
            'password_hash': 'admin123',
            'rol': 'administrador',
            'ultimo_acceso': None,
            'activo': True,
        },
    )


def reverse_initial_data(apps, schema_editor):
    PeriodoAcademico = apps.get_model('api', 'PeriodoAcademico')
    Departamento = apps.get_model('api', 'Departamento')
    Persona = apps.get_model('api', 'Persona')
    Usuario = apps.get_model('api', 'Usuario')

    Usuario.objects.filter(username='admin').delete()
    Persona.objects.filter(numero_doc__in=['10000001', '10000002']).delete()
    Departamento.objects.filter(codigo='INF').delete()
    PeriodoAcademico.objects.filter(nombre='2026 - II').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data, reverse_initial_data),
    ]
