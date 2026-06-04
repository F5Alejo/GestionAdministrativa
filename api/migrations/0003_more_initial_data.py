from datetime import date, time

from django.db import migrations
from django.utils import timezone


def create_more_data(apps, schema_editor):
    PeriodoAcademico = apps.get_model('api', 'PeriodoAcademico')
    Departamento = apps.get_model('api', 'Departamento')
    Edificio = apps.get_model('api', 'Edificio')
    Persona = apps.get_model('api', 'Persona')
    Estudiante = apps.get_model('api', 'Estudiante')
    Docente = apps.get_model('api', 'Docente')
    Programa = apps.get_model('api', 'Programa')
    Curso = apps.get_model('api', 'Curso')
    CursoPrerrequisito = apps.get_model('api', 'CursoPrerrequisito')
    GrupoCurso = apps.get_model('api', 'GrupoCurso')
    Matricula = apps.get_model('api', 'Matricula')
    MatriculaHistorial = apps.get_model('api', 'MatriculaHistorial')
    Evaluacion = apps.get_model('api', 'Evaluacion')
    NotaEvaluacion = apps.get_model('api', 'NotaEvaluacion')
    CalificacionFinal = apps.get_model('api', 'CalificacionFinal')
    Aula = apps.get_model('api', 'Aula')
    Horario = apps.get_model('api', 'Horario')
    Asistencia = apps.get_model('api', 'Asistencia')
    Syllabus = apps.get_model('api', 'Syllabus')
    SyllabusUnidad = apps.get_model('api', 'SyllabusUnidad')
    Tutoria = apps.get_model('api', 'Tutoria')
    MaterialCurso = apps.get_model('api', 'MaterialCurso')
    EventoCalendario = apps.get_model('api', 'EventoCalendario')
    BecaEstudiante = apps.get_model('api', 'BecaEstudiante')
    Pago = apps.get_model('api', 'Pago')
    Homologacion = apps.get_model('api', 'Homologacion')
    SolicitudAcademica = apps.get_model('api', 'SolicitudAcademica')
    Sancion = apps.get_model('api', 'Sancion')
    Usuario = apps.get_model('api', 'Usuario')
    Auditoria = apps.get_model('api', 'Auditoria')

    periodos = [
        {'nombre': '2025 - II', 'fecha_inicio': '2025-08-01', 'fecha_fin': '2025-12-15', 'activo': False},
        {'nombre': '2027 - II', 'fecha_inicio': '2027-08-01', 'fecha_fin': '2027-12-15', 'activo': False},
    ]
    for data in periodos:
        PeriodoAcademico.objects.get_or_create(nombre=data['nombre'], defaults=data)

    periodo_2025_ii = PeriodoAcademico.objects.get(nombre='2025 - II')
    periodo_2026_i, _ = PeriodoAcademico.objects.get_or_create(
        nombre='2026 - I',
        defaults={
            'fecha_inicio': '2026-01-10',
            'fecha_fin': '2026-05-20',
            'activo': True,
        },
    )

    departamentos = [
        {'codigo': 'FIS', 'nombre': 'Física'},
        {'codigo': 'BIO', 'nombre': 'Biología'},
    ]
    for data in departamentos:
        Departamento.objects.get_or_create(codigo=data['codigo'], defaults=data)

    departamento_inf, _ = Departamento.objects.get_or_create(codigo='INF', defaults={'nombre': 'Ingeniería Informática'})
    departamento_fis = Departamento.objects.get(codigo='FIS')
    departamento_bio = Departamento.objects.get(codigo='BIO')

    edificios = [
        {'nombre': 'Edificio D', 'direccion': 'Calle 99 #22-11'},
        {'nombre': 'Edificio E', 'direccion': 'Carrera 10 #55-60'},
    ]
    for data in edificios:
        Edificio.objects.get_or_create(nombre=data['nombre'], defaults=data)

    personas_extra = [
        {'tipo_doc': 'CC', 'numero_doc': '10000007', 'nombres': 'Daniel', 'apellidos': 'Torres', 'fecha_nac': '2000-04-15', 'genero': 'M', 'email': 'daniel.torres@example.com', 'telefono': '3009998888', 'direccion': 'Calle 12', 'ciudad': 'Bucaramanga', 'activo': True},
        {'tipo_doc': 'CC', 'numero_doc': '10000008', 'nombres': 'Carolina', 'apellidos': 'Vega', 'fecha_nac': '2001-06-30', 'genero': 'F', 'email': 'carolina.vega@example.com', 'telefono': '3012223333', 'direccion': 'Carrera 11', 'ciudad': 'Cali', 'activo': True},
        {'tipo_doc': 'CC', 'numero_doc': '10000009', 'nombres': 'Gabriel', 'apellidos': 'Ruiz', 'fecha_nac': '1997-12-04', 'genero': 'M', 'email': 'gabriel.ruiz@example.com', 'telefono': '3023334444', 'direccion': 'Av. 77', 'ciudad': 'Medellín', 'activo': True},
        {'tipo_doc': 'CC', 'numero_doc': '10000010', 'nombres': 'Sofía', 'apellidos': 'Mendoza', 'fecha_nac': '1990-10-01', 'genero': 'F', 'email': 'sofia.mendoza@example.com', 'telefono': '3034445555', 'direccion': 'Calle 23', 'ciudad': 'Bogotá', 'activo': True},
    ]

    personas_objs = []
    for data in personas_extra:
        persona, _ = Persona.objects.get_or_create(tipo_doc=data['tipo_doc'], numero_doc=data['numero_doc'], defaults=data)
        personas_objs.append(persona)

    estudiantes = []
    for index, persona in enumerate(personas_objs[:2], start=1):
        estudiante, _ = Estudiante.objects.get_or_create(persona=persona, defaults={'codigo': f'ESTU-00{index + 3}', 'fecha_ingreso': '2024-02-01', 'activo': True})
        estudiantes.append(estudiante)

    docentes = []
    for index, persona in enumerate(personas_objs[2:], start=4):
        docente, _ = Docente.objects.get_or_create(persona=persona, defaults={'codigo': f'DOC-0{index}', 'departamento': departamento_inf, 'titulo_maximo': 'Especialista', 'dedicacion': 'Tiempo parcial', 'rol': 'Instructor', 'fecha_vinculacion': '2021-03-10', 'activo': True})
        docentes.append(docente)

    programas = []
    programas_data = [
        {'codigo': 'FIS-2026', 'nombre': 'Física', 'departamento': departamento_fis, 'director': docentes[0]},
        {'codigo': 'BIO-2026', 'nombre': 'Biología', 'departamento': departamento_bio, 'director': docentes[1]},
    ]
    for data in programas_data:
        programa, _ = Programa.objects.get_or_create(codigo=data['codigo'], defaults={**data, 'nivel_formacion': 'Pregrado', 'modalidad': 'Presencial', 'creditos_totales': 140, 'duracion_semestres': 9, 'activo': True, 'descripcion': 'Programa académico.'})
        programas.append(programa)

    cursos = []
    cursos_data = [
        {'codigo': 'FIS101', 'nombre': 'Física I', 'programa': programas[0], 'departamento': departamento_fis},
        {'codigo': 'BIO101', 'nombre': 'Biología I', 'programa': programas[1], 'departamento': departamento_bio},
    ]
    for data in cursos_data:
        curso, _ = Curso.objects.get_or_create(codigo=data['codigo'], defaults={**data, 'creditos': 4, 'horas_semana': 4, 'nivel_semestre': 1, 'electiva': False, 'activo': True, 'descripcion': 'Curso introductorio.'})
        cursos.append(curso)

    GrupoCurso.objects.get_or_create(curso=cursos[0], periodo=PeriodoAcademico.objects.get(nombre='2025 - II'), nombre_grupo='D', defaults={'docente': docentes[0], 'modalidad': 'Presencial', 'cupo_maximo': 25})
    GrupoCurso.objects.get_or_create(curso=cursos[1], periodo=PeriodoAcademico.objects.get(nombre='2025 - II'), nombre_grupo='E', defaults={'docente': docentes[1], 'modalidad': 'Virtual', 'cupo_maximo': 25})

    Aula.objects.get_or_create(nombre='Aula 404', defaults={'edificio': Edificio.objects.get(nombre='Edificio D'), 'capacidad': 45, 'tiene_proyector': True, 'tiene_internet': True, 'activa': True})
    Aula.objects.get_or_create(nombre='Aula 505', defaults={'edificio': Edificio.objects.get(nombre='Edificio E'), 'capacidad': 30, 'tiene_proyector': False, 'tiene_internet': True, 'activa': True})

    grupos_extra = list(GrupoCurso.objects.filter(nombre_grupo__in=['D', 'E']))
    matriculas_extra = []
    for i, estudiante in enumerate(estudiantes, start=1):
        matricula, _ = Matricula.objects.get_or_create(estudiante=estudiante, grupo=grupos_extra[i - 1], defaults={'periodo': PeriodoAcademico.objects.get(nombre='2025 - II'), 'estado': 'Activa', 'fecha_matricula': timezone.now(), 'nota_final': 4.0})
        matriculas_extra.append(matricula)

    for matricula in matriculas_extra:
        MatriculaHistorial.objects.get_or_create(
            matricula=matricula,
            estado_nuevo='Activa',
            defaults={
                'fecha_cambio': timezone.now(),
                'motivo': 'Registro adicional',
                'registrado_por': personas_objs[0],
            },
        )

    evaluaciones_extra = [
        {'grupo': grupos_extra[0], 'nombre': 'Parcial 3', 'tipo': 'Parcial', 'fecha_aplicacion': '2025-09-15', 'porcentaje': 30.0},
        {'grupo': grupos_extra[1], 'nombre': 'Proyecto Final', 'tipo': 'Proyecto', 'fecha_aplicacion': '2025-10-20', 'porcentaje': 40.0},
    ]
    evaluaciones_objs = []
    for data in evaluaciones_extra:
        evaluacion, _ = Evaluacion.objects.get_or_create(grupo=data['grupo'], nombre=data['nombre'], defaults={**data, 'descripcion': 'Evaluación adicional', 'nota_maxima': 5.0})
        evaluaciones_objs.append(evaluacion)

    NotaEvaluacion.objects.get_or_create(evaluacion=evaluaciones_objs[0], estudiante=estudiantes[0], defaults={'nota': 4.2, 'ausente': False, 'observaciones': 'Buen desempeño', 'registrado_en': timezone.now()})
    NotaEvaluacion.objects.get_or_create(evaluacion=evaluaciones_objs[1], estudiante=estudiantes[1], defaults={'nota': 3.8, 'ausente': False, 'observaciones': 'Proyecto entregado', 'registrado_en': timezone.now()})

    for matricula in matriculas_extra:
        CalificacionFinal.objects.get_or_create(matricula=matricula, defaults={'nota_calculada': 4.1, 'nota_definitiva': 4.0, 'aprobado': True, 'fecha_cierre': timezone.now()})

    Horario.objects.get_or_create(grupo=grupos_extra[0], aula=Aula.objects.get(nombre='Aula 404'), dia='Jueves', hora_inicio=time(8, 0), defaults={'hora_fin': time(10, 0)})
    Horario.objects.get_or_create(grupo=grupos_extra[1], aula=Aula.objects.get(nombre='Aula 505'), dia='Viernes', hora_inicio=time(10, 0), defaults={'hora_fin': time(12, 0)})

    horarios_extra = list(Horario.objects.filter(aula__nombre__in=['Aula 404', 'Aula 505']))
    Asistencia.objects.get_or_create(grupo=grupos_extra[0], estudiante=estudiantes[0], horario=horarios_extra[0], fecha='2025-09-16', defaults={'presente': True, 'justificada': False, 'observacion': 'Asistencia extra'})
    Asistencia.objects.get_or_create(grupo=grupos_extra[1], estudiante=estudiantes[1], horario=horarios_extra[1], fecha='2025-09-17', defaults={'presente': True, 'justificada': False, 'observacion': 'Asistencia extra'})

    for grupo in grupos_extra:
        Syllabus.objects.get_or_create(grupo=grupo, defaults={'objetivo_general': 'Objetivo adicional.', 'metodologia': 'Talleres prácticos.', 'bibliografia': 'Artículos y documentos.', 'creado_en': timezone.now()})

    for index, syllabus in enumerate(Syllabus.objects.filter(grupo__in=grupos_extra), start=1):
        SyllabusUnidad.objects.get_or_create(syllabus=syllabus, numero=index, defaults={'titulo': f'Unidad extra {index}', 'contenido': 'Contenido adicional.', 'semanas_duracion': 1})

    Tutoria.objects.get_or_create(docente=docentes[0], estudiante=estudiantes[0], fecha=timezone.now(), defaults={'curso': cursos[0], 'duracion_min': 30, 'modalidad': 'Virtual', 'observaciones': 'Tutoria adicional'})
    Tutoria.objects.get_or_create(docente=docentes[1], estudiante=estudiantes[1], fecha=timezone.now(), defaults={'curso': cursos[1], 'duracion_min': 40, 'modalidad': 'Presencial', 'observaciones': 'Tutoria adicional'})

    MaterialCurso.objects.get_or_create(grupo=grupos_extra[0], titulo='Manual avanzado', defaults={'tipo': 'PDF', 'url': 'https://example.com/manual', 'descripcion': 'Material extra', 'publicado_en': timezone.now()})
    MaterialCurso.objects.get_or_create(grupo=grupos_extra[1], titulo='Tarea práctica', defaults={'tipo': 'Documento', 'url': 'https://example.com/tarea', 'descripcion': 'Material extra', 'publicado_en': timezone.now()})

    EventoCalendario.objects.get_or_create(titulo='Jornada de bienestar', defaults={'descripcion': 'Evento estudiantil.', 'fecha_inicio': '2025-09-10 09:00', 'fecha_fin': '2025-09-10 12:00', 'tipo': 'Bienestar', 'aplica_todos': True, 'programa': programas[0]})
    EventoCalendario.objects.get_or_create(titulo='Seminario de investigación', defaults={'descripcion': 'Evento académico.', 'fecha_inicio': '2025-10-05 10:00', 'fecha_fin': '2025-10-05 13:00', 'tipo': 'Seminario', 'aplica_todos': False, 'programa': programas[1]})

    BecaEstudiante.objects.get_or_create(estudiante=estudiantes[0], periodo=periodo_2026_i, tipo_beca='Cultural', defaults={'porcentaje_descuento': 20.0, 'aprobado': True, 'fecha_aprobacion': '2026-01-25', 'observaciones': 'Beca cultural'})
    BecaEstudiante.objects.get_or_create(estudiante=estudiantes[1], periodo=periodo_2026_i, tipo_beca='Académica', defaults={'porcentaje_descuento': 25.0, 'aprobado': True, 'fecha_aprobacion': '2026-01-26', 'observaciones': 'Beca académica'})

    Pago.objects.get_or_create(estudiante=estudiantes[0], periodo=periodo_2026_i, referencia='PAGO4', defaults={'monto': '1300000.00', 'metodo': 'Efectivo', 'estado': 'Confirmado', 'fecha_pago': timezone.now()})
    Pago.objects.get_or_create(estudiante=estudiantes[1], periodo=periodo_2026_i, referencia='PAGO5', defaults={'monto': '1100000.00', 'metodo': 'Tarjeta', 'estado': 'Confirmado', 'fecha_pago': timezone.now()})

    Homologacion.objects.get_or_create(estudiante=estudiantes[0], curso_origen='Física básica', defaults={'institucion_origen': 'Colegio A', 'curso_destino': Curso.objects.get(codigo='FIS101'), 'nota_origen': '4.2', 'aprobado': True, 'fecha_solicitud': date.today()})
    Homologacion.objects.get_or_create(estudiante=estudiantes[1], curso_origen='Biología general', defaults={'institucion_origen': 'Colegio B', 'curso_destino': Curso.objects.get(codigo='BIO101'), 'nota_origen': '4.0', 'aprobado': False, 'fecha_solicitud': date.today()})

    SolicitudAcademica.objects.get_or_create(estudiante=estudiantes[0], tipo='Homologación', defaults={'descripcion': 'Solicita homologar curso.', 'estado': 'Pendiente', 'fecha_envio': timezone.now(), 'atendida_por': personas_objs[2]})
    SolicitudAcademica.objects.get_or_create(estudiante=estudiantes[1], tipo='Cambio de horario', defaults={'descripcion': 'Solicita cambio de horario.', 'estado': 'Aprobada', 'fecha_envio': timezone.now(), 'fecha_respuesta': timezone.now(), 'respuesta': 'Cambiado.', 'atendida_por': personas_objs[3]})

    Sancion.objects.get_or_create(estudiante=estudiantes[0], tipo='Inasistencia', defaults={'descripcion': 'Faltó a clase.', 'fecha': date.today(), 'resuelto': False})
    Sancion.objects.get_or_create(estudiante=estudiantes[1], tipo='Trabajo incompleto', defaults={'descripcion': 'No entregó trabajo.', 'fecha': date.today(), 'resuelto': True})

    Usuario.objects.get_or_create(username='user1', defaults={'persona': personas_objs[0], 'password_hash': 'user1pass', 'rol': 'estudiante', 'activo': True, 'ultimo_acceso': None, 'creado_en': timezone.now()})
    Usuario.objects.get_or_create(username='user2', defaults={'persona': personas_objs[1], 'password_hash': 'user2pass', 'rol': 'estudiante', 'activo': True, 'ultimo_acceso': None, 'creado_en': timezone.now()})

    Auditoria.objects.get_or_create(tabla='usuarios', operacion='C', registro_id=1, defaults={'usuario': Usuario.objects.filter(username='user1').first(), 'datos_antes': None, 'datos_despues': {'username': 'user1'}, 'fecha': timezone.now()})
    Auditoria.objects.get_or_create(tabla='usuarios', operacion='C', registro_id=2, defaults={'usuario': Usuario.objects.filter(username='user2').first(), 'datos_antes': None, 'datos_despues': {'username': 'user2'}, 'fecha': timezone.now()})


def reverse_more_data(apps, schema_editor):
    PeriodoAcademico = apps.get_model('api', 'PeriodoAcademico')
    Departamento = apps.get_model('api', 'Departamento')
    Edificio = apps.get_model('api', 'Edificio')
    Persona = apps.get_model('api', 'Persona')
    Usuario = apps.get_model('api', 'Usuario')

    Auditoria.objects.filter(tabla='usuarios', registro_id__in=[1, 2]).delete()
    Usuario.objects.filter(username__in=['user1', 'user2']).delete()
    Persona.objects.filter(numero_doc__in=['10000007', '10000008', '10000009', '10000010']).delete()
    Edificio.objects.filter(nombre__in=['Edificio D', 'Edificio E']).delete()
    Departamento.objects.filter(codigo__in=['FIS', 'BIO']).delete()
    PeriodoAcademico.objects.filter(nombre__in=['2025 - II', '2027 - II']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial_data'),
    ]

    operations = [
        migrations.RunPython(create_more_data, reverse_more_data),
    ]
