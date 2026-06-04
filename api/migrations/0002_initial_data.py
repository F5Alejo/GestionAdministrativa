from datetime import date, time

from django.db import migrations
from django.utils import timezone


def create_initial_data(apps, schema_editor):
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
        {
            'nombre': '2026 - I',
            'fecha_inicio': '2026-01-10',
            'fecha_fin': '2026-05-20',
            'activo': True,
        },
        {
            'nombre': '2026 - II',
            'fecha_inicio': '2026-08-01',
            'fecha_fin': '2026-12-15',
            'activo': True,
        },
        {
            'nombre': '2027 - I',
            'fecha_inicio': '2027-01-11',
            'fecha_fin': '2027-05-22',
            'activo': False,
        },
    ]

    departamentos = [
        {'codigo': 'INF', 'nombre': 'Ingeniería Informática'},
        {'codigo': 'ADM', 'nombre': 'Administración'},
        {'codigo': 'MAT', 'nombre': 'Matemáticas'},
    ]

    edificios = [
        {'nombre': 'Edificio A', 'direccion': 'Calle 1 #10-20'},
        {'nombre': 'Edificio B', 'direccion': 'Carrera 5 #20-30'},
        {'nombre': 'Edificio C', 'direccion': 'Av. Central #50-60'},
    ]

    personas_data = [
        {
            'tipo_doc': 'CC',
            'numero_doc': '10000001',
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
        {
            'tipo_doc': 'CC',
            'numero_doc': '10000002',
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
        {
            'tipo_doc': 'CC',
            'numero_doc': '10000003',
            'nombres': 'Luis',
            'apellidos': 'Martínez',
            'fecha_nac': '1999-09-12',
            'genero': 'M',
            'email': 'luis.martinez@example.com',
            'telefono': '3201239876',
            'direccion': 'Calle 45',
            'ciudad': 'Cali',
            'activo': True,
        },
        {
            'tipo_doc': 'CC',
            'numero_doc': '10000004',
            'nombres': 'Ana',
            'apellidos': 'Ramírez',
            'fecha_nac': '1978-11-08',
            'genero': 'F',
            'email': 'ana.ramirez@example.com',
            'telefono': '3169876543',
            'direccion': 'Av. 20',
            'ciudad': 'Cartagena',
            'activo': True,
        },
        {
            'tipo_doc': 'CC',
            'numero_doc': '10000005',
            'nombres': 'Pedro',
            'apellidos': 'López',
            'fecha_nac': '2001-02-28',
            'genero': 'M',
            'email': 'pedro.lopez@example.com',
            'telefono': '3151112222',
            'direccion': 'Calle 67',
            'ciudad': 'Bucaramanga',
            'activo': True,
        },
        {
            'tipo_doc': 'CC',
            'numero_doc': '10000006',
            'nombres': 'Luisa',
            'apellidos': 'Suárez',
            'fecha_nac': '1998-07-19',
            'genero': 'F',
            'email': 'luisa.suarez@example.com',
            'telefono': '3175556667',
            'direccion': 'Calle 88',
            'ciudad': 'Pereira',
            'activo': True,
        },
    ]

    periodos_objs = []
    for periodo_data in periodos:
        periodo, _ = PeriodoAcademico.objects.get_or_create(
            nombre=periodo_data['nombre'],
            defaults=periodo_data,
        )
        periodos_objs.append(periodo)

    departamentos_objs = []
    for departamento_data in departamentos:
        departamento, _ = Departamento.objects.get_or_create(
            codigo=departamento_data['codigo'],
            defaults=departamento_data,
        )
        departamentos_objs.append(departamento)

    edificios_objs = []
    for edificio_data in edificios:
        edificio, _ = Edificio.objects.get_or_create(
            nombre=edificio_data['nombre'],
            defaults=edificio_data,
        )
        edificios_objs.append(edificio)

    personas = []
    for persona_data in personas_data:
        persona, _ = Persona.objects.get_or_create(
            tipo_doc=persona_data['tipo_doc'],
            numero_doc=persona_data['numero_doc'],
            defaults=persona_data,
        )
        personas.append(persona)

    estudiantes = []
    for index, persona in enumerate(personas[:3], start=1):
        estudiante, _ = Estudiante.objects.get_or_create(
            persona=persona,
            defaults={
                'codigo': f'ESTU-000{index}',
                'fecha_ingreso': '2024-01-15',
                'activo': True,
            },
        )
        estudiantes.append(estudiante)

    docentes = []
    for index, persona in enumerate(personas[3:], start=1):
        docente, _ = Docente.objects.get_or_create(
            persona=persona,
            defaults={
                'codigo': f'DOC-00{index}',
                'departamento': departamentos_objs[0],
                'titulo_maximo': 'Magíster en Ciencias de la Computación',
                'dedicacion': 'Tiempo completo',
                'rol': 'Profesor',
                'fecha_vinculacion': '2020-02-01',
                'activo': True,
            },
        )
        docentes.append(docente)

    programas = []
    for index, codigo in enumerate(['INF-2026', 'ADM-2026', 'MAT-2026'], start=1):
        programa, _ = Programa.objects.get_or_create(
            codigo=codigo,
            defaults={
                'nombre': 'Ingeniería Informática' if index == 1 else 'Administración' if index == 2 else 'Matemáticas',
                'nivel_formacion': 'Pregrado',
                'departamento': departamentos_objs[index - 1],
                'director': docentes[index - 1],
                'modalidad': 'Presencial',
                'creditos_totales': 160,
                'duracion_semestres': 10,
                'activo': True,
                'descripcion': 'Programa de formación profesional.',
            },
        )
        programas.append(programa)

    cursos = []
    cursos_data = [
        {'codigo': 'INF101', 'nombre': 'Fundamentos de Programación', 'programa': programas[0], 'departamento': departamentos_objs[0], 'nivel_semestre': 1},
        {'codigo': 'ADM101', 'nombre': 'Introducción a la Administración', 'programa': programas[1], 'departamento': departamentos_objs[1], 'nivel_semestre': 1},
        {'codigo': 'MAT101', 'nombre': 'Álgebra Lineal', 'programa': programas[2], 'departamento': departamentos_objs[2], 'nivel_semestre': 1},
    ]
    for curso_data in cursos_data:
        curso, _ = Curso.objects.get_or_create(
            codigo=curso_data['codigo'],
            defaults={
                'programa': curso_data['programa'],
                'departamento': curso_data['departamento'],
                'nombre': curso_data['nombre'],
                'creditos': 4,
                'horas_semana': 4,
                'nivel_semestre': curso_data['nivel_semestre'],
                'electiva': False,
                'activo': True,
                'descripcion': f'Curso de {curso_data["nombre"]}.',
            },
        )
        cursos.append(curso)

    CursoPrerrequisito.objects.get_or_create(curso=cursos[0], prerrequisito=cursos[2])
    CursoPrerrequisito.objects.get_or_create(curso=cursos[1], prerrequisito=cursos[2])
    CursoPrerrequisito.objects.get_or_create(curso=cursos[0], prerrequisito=cursos[1])

    grupos = []
    for index, curso in enumerate(cursos, start=1):
        grupo, _ = GrupoCurso.objects.get_or_create(
            curso=curso,
            periodo=periodos_objs[0],
            nombre_grupo=chr(64 + index),
            defaults={
                'docente': docentes[index - 1],
                'modalidad': 'Presencial',
                'cupo_maximo': 30,
            },
        )
        grupos.append(grupo)

    aulas = []
    aulas_data = [
        {'nombre': 'Aula 101', 'edificio': edificios_objs[0], 'capacidad': 40, 'tiene_proyector': True, 'tiene_internet': True},
        {'nombre': 'Aula 202', 'edificio': edificios_objs[1], 'capacidad': 35, 'tiene_proyector': False, 'tiene_internet': True},
        {'nombre': 'Aula 303', 'edificio': edificios_objs[2], 'capacidad': 50, 'tiene_proyector': True, 'tiene_internet': False},
    ]
    for aula_data in aulas_data:
        aula, _ = Aula.objects.get_or_create(
            nombre=aula_data['nombre'],
            defaults=aula_data,
        )
        aulas.append(aula)

    matriculas = []
    for index, estudiante in enumerate(estudiantes, start=1):
        matricula, _ = Matricula.objects.get_or_create(
            estudiante=estudiante,
            grupo=grupos[index - 1],
            defaults={
                'periodo': periodos_objs[0],
                'estado': 'Activa',
                'fecha_matricula': timezone.now(),
                'nota_final': 4.5,
            },
        )
        matriculas.append(matricula)

    for index, matricula in enumerate(matriculas, start=1):
        MatriculaHistorial.objects.get_or_create(
            matricula=matricula,
            estado_nuevo='Activa',
            defaults={
                'fecha_cambio': timezone.now(),
                'motivo': 'Matrícula inicial',
                'registrado_por': personas[index],
            },
        )

    evaluaciones = []
    evaluaciones_data = [
        {'grupo': grupos[0], 'tipo': 'Parcial', 'nombre': 'Parcial 1', 'fecha_aplicacion': '2026-03-15', 'porcentaje': 30.0},
        {'grupo': grupos[1], 'tipo': 'Parcial', 'nombre': 'Parcial 2', 'fecha_aplicacion': '2026-03-20', 'porcentaje': 30.0},
        {'grupo': grupos[2], 'tipo': 'Seminario', 'nombre': 'Exposición', 'fecha_aplicacion': '2026-03-25', 'porcentaje': 20.0},
    ]
    for evaluacion_data in evaluaciones_data:
        evaluacion, _ = Evaluacion.objects.get_or_create(
            grupo=evaluacion_data['grupo'],
            nombre=evaluacion_data['nombre'],
            defaults={
                'tipo': evaluacion_data['tipo'],
                'descripcion': f'Evaluación {evaluacion_data["nombre"]}',
                'fecha_aplicacion': evaluacion_data['fecha_aplicacion'],
                'porcentaje': evaluacion_data['porcentaje'],
                'nota_maxima': 5.0,
            },
        )
        evaluaciones.append(evaluacion)

    for index, evaluacion in enumerate(evaluaciones, start=1):
        NotaEvaluacion.objects.get_or_create(
            evaluacion=evaluacion,
            estudiante=estudiantes[index - 1],
            defaults={
                'nota': 4.0 + index * 0.2,
                'ausente': False,
                'observaciones': 'Entrega correcta',
                'registrado_en': timezone.now(),
            },
        )

    for matricula in matriculas:
        CalificacionFinal.objects.get_or_create(
            matricula=matricula,
            defaults={
                'nota_calculada': 4.3,
                'nota_definitiva': 4.2,
                'aprobado': True,
                'fecha_cierre': timezone.now(),
            },
        )

    horarios = []
    horarios_data = [
        {'grupo': grupos[0], 'aula': aulas[0], 'dia': 'Lunes', 'hora_inicio': time(8, 0), 'hora_fin': time(10, 0)},
        {'grupo': grupos[1], 'aula': aulas[1], 'dia': 'Martes', 'hora_inicio': time(10, 0), 'hora_fin': time(12, 0)},
        {'grupo': grupos[2], 'aula': aulas[2], 'dia': 'Miércoles', 'hora_inicio': time(14, 0), 'hora_fin': time(16, 0)},
    ]
    for horario_data in horarios_data:
        horario, _ = Horario.objects.get_or_create(
            grupo=horario_data['grupo'],
            aula=horario_data['aula'],
            dia=horario_data['dia'],
            hora_inicio=horario_data['hora_inicio'],
            defaults={'hora_fin': horario_data['hora_fin']},
        )
        horarios.append(horario)

    for index, horario in enumerate(horarios, start=1):
        Asistencia.objects.get_or_create(
            grupo=horario.grupo,
            estudiante=estudiantes[index - 1],
            horario=horario,
            fecha='2026-03-16',
            defaults={
                'presente': True,
                'justificada': False,
                'observacion': 'Asistencia registrada',
            },
        )

    syllabi = []
    for grupo in grupos:
        syllabus, _ = Syllabus.objects.get_or_create(
            grupo=grupo,
            defaults={
                'objetivo_general': 'Desarrollar competencias académicas.',
                'metodologia': 'Clases teóricas y prácticas.',
                'bibliografia': 'Libro de texto, artículos.',
                'creado_en': timezone.now(),
            },
        )
        syllabi.append(syllabus)

    for index, syllabus in enumerate(syllabi, start=1):
        SyllabusUnidad.objects.get_or_create(
            syllabus=syllabus,
            numero=index,
            defaults={
                'titulo': f'Unidad {index}',
                'contenido': 'Temas principales del curso.',
                'semanas_duracion': 2,
            },
        )

    tutorias_data = [
        {'docente': docentes[0], 'estudiante': estudiantes[0], 'curso': cursos[0], 'duracion_min': 60, 'modalidad': 'Presencial', 'observaciones': 'Revisión de avance.'},
        {'docente': docentes[1], 'estudiante': estudiantes[1], 'curso': cursos[1], 'duracion_min': 45, 'modalidad': 'Virtual', 'observaciones': 'Planeación de proyecto.'},
        {'docente': docentes[2], 'estudiante': estudiantes[2], 'curso': cursos[2], 'duracion_min': 30, 'modalidad': 'Presencial', 'observaciones': 'Asesoría de tareas.'},
    ]
    for data in tutorias_data:
        Tutoria.objects.get_or_create(
            docente=data['docente'],
            estudiante=data['estudiante'],
            fecha=timezone.now(),
            defaults={
                'curso': data['curso'],
                'duracion_min': data['duracion_min'],
                'modalidad': data['modalidad'],
                'observaciones': data['observaciones'],
            },
        )

    materiales_data = [
        {'grupo': grupos[0], 'titulo': 'Guía de ejercicios', 'tipo': 'Documento', 'url': 'https://example.com/guia', 'descripcion': 'Material de apoyo.'},
        {'grupo': grupos[1], 'titulo': 'Presentación introductoria', 'tipo': 'PPT', 'url': 'https://example.com/presentacion', 'descripcion': 'Slides de clase.'},
        {'grupo': grupos[2], 'titulo': 'Video tutorial', 'tipo': 'Video', 'url': 'https://example.com/video', 'descripcion': 'Sesión grabada.'},
    ]
    for data in materiales_data:
        MaterialCurso.objects.get_or_create(
            grupo=data['grupo'],
            titulo=data['titulo'],
            defaults={
                'tipo': data['tipo'],
                'url': data['url'],
                'descripcion': data['descripcion'],
                'publicado_en': timezone.now(),
            },
        )

    eventos_data = [
        {'titulo': 'Inicio de semestre', 'fecha_inicio': '2026-01-10 08:00', 'fecha_fin': '2026-01-10 12:00', 'tipo': 'Evento académico', 'programa': programas[0]},
        {'titulo': 'Feria de empleo', 'fecha_inicio': '2026-02-20 09:00', 'fecha_fin': '2026-02-20 14:00', 'tipo': 'Feria', 'programa': programas[1]},
        {'titulo': 'Conferencia matemática', 'fecha_inicio': '2026-03-05 10:00', 'fecha_fin': '2026-03-05 12:00', 'tipo': 'Conferencia', 'programa': programas[2]},
    ]
    for data in eventos_data:
        EventoCalendario.objects.get_or_create(
            titulo=data['titulo'],
            defaults={
                'descripcion': 'Evento del calendario académico.',
                'fecha_inicio': data['fecha_inicio'],
                'fecha_fin': data['fecha_fin'],
                'tipo': data['tipo'],
                'aplica_todos': False,
                'programa': data['programa'],
            },
        )

    becas_data = [
        {'estudiante': estudiantes[0], 'periodo': periodos_objs[0], 'tipo_beca': 'Meritocrática', 'porcentaje_descuento': 50.0, 'aprobado': True, 'fecha_aprobacion': '2026-01-20'},
        {'estudiante': estudiantes[1], 'periodo': periodos_objs[0], 'tipo_beca': 'Deportiva', 'porcentaje_descuento': 40.0, 'aprobado': True, 'fecha_aprobacion': '2026-01-22'},
        {'estudiante': estudiantes[2], 'periodo': periodos_objs[0], 'tipo_beca': 'Socioeconómica', 'porcentaje_descuento': 30.0, 'aprobado': False, 'fecha_aprobacion': None},
    ]
    for data in becas_data:
        BecaEstudiante.objects.get_or_create(
            estudiante=data['estudiante'],
            tipo_beca=data['tipo_beca'],
            periodo=data['periodo'],
            defaults={
                'porcentaje_descuento': data['porcentaje_descuento'],
                'aprobado': data['aprobado'],
                'fecha_aprobacion': data['fecha_aprobacion'],
                'observaciones': 'Beca asignada.',
            },
        )

    pagos_data = [
        {'estudiante': estudiantes[0], 'periodo': periodos_objs[0], 'monto': '1500000.00', 'metodo': 'Transferencia', 'referencia': 'PAGO1', 'estado': 'Confirmado'},
        {'estudiante': estudiantes[1], 'periodo': periodos_objs[0], 'monto': '1200000.00', 'metodo': 'Efectivo', 'referencia': 'PAGO2', 'estado': 'Confirmado'},
        {'estudiante': estudiantes[2], 'periodo': periodos_objs[0], 'monto': '1000000.00', 'metodo': 'Tarjeta', 'referencia': 'PAGO3', 'estado': 'Pendiente'},
    ]
    for data in pagos_data:
        Pago.objects.get_or_create(
            estudiante=data['estudiante'],
            periodo=data['periodo'],
            referencia=data['referencia'],
            defaults={
                'monto': data['monto'],
                'metodo': data['metodo'],
                'estado': data['estado'],
                'fecha_pago': timezone.now(),
            },
        )

    homologaciones_data = [
        {'estudiante': estudiantes[0], 'curso_origen': 'Programación I', 'institucion_origen': 'Universidad X', 'curso_destino': cursos[0], 'nota_origen': '4.0', 'aprobado': True},
        {'estudiante': estudiantes[1], 'curso_origen': 'Administración básica', 'institucion_origen': 'Instituto Y', 'curso_destino': cursos[1], 'nota_origen': '4.5', 'aprobado': True},
        {'estudiante': estudiantes[2], 'curso_origen': 'Cálculo I', 'institucion_origen': 'Colegio Z', 'curso_destino': cursos[2], 'nota_origen': '3.8', 'aprobado': False},
    ]
    for data in homologaciones_data:
        Homologacion.objects.get_or_create(
            estudiante=data['estudiante'],
            curso_origen=data['curso_origen'],
            defaults={
                'institucion_origen': data['institucion_origen'],
                'curso_destino': data['curso_destino'],
                'nota_origen': data['nota_origen'],
                'aprobado': data['aprobado'],
                'fecha_solicitud': date.today(),
            },
        )

    solicitudes_data = [
        {'estudiante': estudiantes[0], 'tipo': 'Cambio de grupo', 'descripcion': 'Solicita cambio de grupo.', 'estado': 'Pendiente', 'atendida_por': personas[3]},
        {'estudiante': estudiantes[1], 'tipo': 'Certificado', 'descripcion': 'Solicita certificado académico.', 'estado': 'Aprobada', 'fecha_respuesta': timezone.now(), 'respuesta': 'Certificado listo.', 'atendida_por': personas[4]},
        {'estudiante': estudiantes[2], 'tipo': 'Prórroga', 'descripcion': 'Solicita extensión de plazo.', 'estado': 'Rechazada', 'fecha_respuesta': timezone.now(), 'respuesta': 'No procede.', 'atendida_por': personas[5]},
    ]
    for data in solicitudes_data:
        SolicitudAcademica.objects.get_or_create(
            estudiante=data['estudiante'],
            tipo=data['tipo'],
            defaults={
                'descripcion': data['descripcion'],
                'estado': data['estado'],
                'fecha_envio': timezone.now(),
                'fecha_respuesta': data.get('fecha_respuesta'),
                'respuesta': data.get('respuesta'),
                'atendida_por': data['atendida_por'],
            },
        )

    sanciones_data = [
        {'estudiante': estudiantes[0], 'tipo': 'Retraso', 'descripcion': 'Llegada tarde a clase.', 'resuelto': True},
        {'estudiante': estudiantes[1], 'tipo': 'Falta de entrega', 'descripcion': 'No entregó tarea.', 'resuelto': False},
        {'estudiante': estudiantes[2], 'tipo': 'Orden', 'descripcion': 'Comportamiento inapropiado.', 'resuelto': False},
    ]
    for data in sanciones_data:
        Sancion.objects.get_or_create(
            estudiante=data['estudiante'],
            tipo=data['tipo'],
            defaults={
                'descripcion': data['descripcion'],
                'fecha': date.today(),
                'resuelto': data['resuelto'],
            },
        )

    usuarios_data = [
        {'persona': personas[3], 'username': 'admin', 'password_hash': 'admin123', 'rol': 'administrador'},
        {'persona': personas[4], 'username': 'gestor', 'password_hash': 'gestor123', 'rol': 'gestor'},
        {'persona': personas[5], 'username': 'docente', 'password_hash': 'docente123', 'rol': 'docente'},
    ]
    usuarios = []
    for data in usuarios_data:
        usuario, _ = Usuario.objects.get_or_create(
            username=data['username'],
            defaults={
                'persona': data['persona'],
                'password_hash': data['password_hash'],
                'rol': data['rol'],
                'activo': True,
                'ultimo_acceso': None,
                'creado_en': timezone.now(),
            },
        )
        usuarios.append(usuario)

    for index, usuario in enumerate(usuarios, start=1):
        Auditoria.objects.get_or_create(
            tabla='usuarios',
            operacion='C',
            registro_id=usuario.usuario_id,
            defaults={
                'usuario': usuario,
                'datos_antes': None,
                'datos_despues': {'username': usuario.username, 'rol': usuario.rol},
                'fecha': timezone.now(),
            },
        )


def reverse_initial_data(apps, schema_editor):
    PeriodoAcademico = apps.get_model('api', 'PeriodoAcademico')
    Departamento = apps.get_model('api', 'Departamento')
    Edificio = apps.get_model('api', 'Edificio')
    Persona = apps.get_model('api', 'Persona')
    Usuario = apps.get_model('api', 'Usuario')

    Usuario.objects.filter(username__in=['admin', 'gestor', 'docente']).delete()
    Persona.objects.filter(numero_doc__in=['10000001', '10000002', '10000003', '10000004', '10000005', '10000006']).delete()
    Edificio.objects.filter(nombre__in=['Edificio A', 'Edificio B', 'Edificio C']).delete()
    Departamento.objects.filter(codigo__in=['INF', 'ADM', 'MAT']).delete()
    PeriodoAcademico.objects.filter(nombre__in=['2026 - I', '2026 - II', '2027 - I']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data, reverse_initial_data),
    ]
