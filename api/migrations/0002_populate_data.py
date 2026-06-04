# Generated migration for seeding initial data
# Compatible with Django 6.0.6

import datetime
from django.db import migrations


def insertar_datos(apps, schema_editor):

    # ── Modelos ──────────────────────────────────────────────
    Departamento     = apps.get_model('api', 'Departamento')
    Edificio         = apps.get_model('api', 'Edificio')
    PeriodoAcademico = apps.get_model('api', 'PeriodoAcademico')
    Persona          = apps.get_model('api', 'Persona')
    Docente          = apps.get_model('api', 'Docente')
    Estudiante       = apps.get_model('api', 'Estudiante')
    Programa         = apps.get_model('api', 'Programa')
    Curso            = apps.get_model('api', 'Curso')
    Aula             = apps.get_model('api', 'Aula')
    GrupoCurso       = apps.get_model('api', 'GrupoCurso')
    Evaluacion       = apps.get_model('api', 'Evaluacion')
    Horario          = apps.get_model('api', 'Horario')
    Matricula        = apps.get_model('api', 'Matricula')
    NotaEvaluacion   = apps.get_model('api', 'NotaEvaluacion')

    # ── 1. DEPARTAMENTOS ─────────────────────────────────────
    dep_sistemas  = Departamento.objects.create(nombre='Ingeniería de Sistemas',     codigo='IS')
    dep_basicas   = Departamento.objects.create(nombre='Ciencias Básicas',           codigo='CB')
    dep_admin     = Departamento.objects.create(nombre='Administración de Empresas', codigo='AE')
    dep_sociales  = Departamento.objects.create(nombre='Ciencias Sociales',          codigo='CS')

    # ── 2. EDIFICIOS ─────────────────────────────────────────
    ed_a = Edificio.objects.create(nombre='Bloque A – Administrativo', direccion='Calle 10 # 5-20')
    ed_b = Edificio.objects.create(nombre='Bloque B – Ingenierías',    direccion='Calle 10 # 5-40')
    ed_c = Edificio.objects.create(nombre='Bloque C – Laboratorios',   direccion='Calle 10 # 5-60')

    # ── 3. PERÍODOS ACADÉMICOS ────────────────────────────────
    p_2024_1 = PeriodoAcademico.objects.create(
        nombre='2024-1', fecha_inicio=datetime.date(2024, 1, 22),
        fecha_fin=datetime.date(2024, 6, 15), activo=False)
    p_2024_2 = PeriodoAcademico.objects.create(
        nombre='2024-2', fecha_inicio=datetime.date(2024, 7, 22),
        fecha_fin=datetime.date(2024, 11, 30), activo=False)
    p_2025_1 = PeriodoAcademico.objects.create(
        nombre='2025-1', fecha_inicio=datetime.date(2025, 1, 20),
        fecha_fin=datetime.date(2025, 6, 14), activo=False)
    p_2025_2 = PeriodoAcademico.objects.create(
        nombre='2025-2', fecha_inicio=datetime.date(2025, 7, 21),
        fecha_fin=datetime.date(2025, 11, 29), activo=True)

    # ── 4. PERSONAS (docentes) ────────────────────────────────
    per_doc1 = Persona.objects.create(
        tipo_doc='CC', numero_doc='10000001',
        nombres='Carlos', apellidos='Ramírez Gómez',
        fecha_nac=datetime.date(1975, 3, 12), genero='M',
        email='carlos.ramirez@universidad.edu.co',
        telefono='3001234567', ciudad='Bogotá')
    per_doc2 = Persona.objects.create(
        tipo_doc='CC', numero_doc='10000002',
        nombres='Ana', apellidos='Torres Medina',
        fecha_nac=datetime.date(1980, 7, 25), genero='F',
        email='ana.torres@universidad.edu.co',
        telefono='3017654321', ciudad='Medellín')
    per_doc3 = Persona.objects.create(
        tipo_doc='CC', numero_doc='10000003',
        nombres='Luis', apellidos='Herrera Ospina',
        fecha_nac=datetime.date(1978, 11, 5), genero='M',
        email='luis.herrera@universidad.edu.co',
        telefono='3109876543', ciudad='Cali')

    # ── 5. PERSONAS (estudiantes) ─────────────────────────────
    per_est1 = Persona.objects.create(
        tipo_doc='CC', numero_doc='20000001',
        nombres='Sofía', apellidos='Castro López',
        fecha_nac=datetime.date(2002, 4, 18), genero='F',
        email='sofia.castro@estudiantes.edu.co',
        telefono='3151112233', ciudad='Bogotá')
    per_est2 = Persona.objects.create(
        tipo_doc='CC', numero_doc='20000002',
        nombres='Juan', apellidos='Moreno Ríos',
        fecha_nac=datetime.date(2001, 9, 30), genero='M',
        email='juan.moreno@estudiantes.edu.co',
        telefono='3162223344', ciudad='Bogotá')
    per_est3 = Persona.objects.create(
        tipo_doc='TI', numero_doc='20000003',
        nombres='Valentina', apellidos='Salcedo Ruiz',
        fecha_nac=datetime.date(2003, 1, 7), genero='F',
        email='valentina.salcedo@estudiantes.edu.co',
        telefono='3173334455', ciudad='Bucaramanga')
    per_est4 = Persona.objects.create(
        tipo_doc='CC', numero_doc='20000004',
        nombres='Andrés', apellidos='Vargas Peña',
        fecha_nac=datetime.date(2000, 6, 22), genero='M',
        email='andres.vargas@estudiantes.edu.co',
        telefono='3184445566', ciudad='Cali')
    per_est5 = Persona.objects.create(
        tipo_doc='TI', numero_doc='20000005',
        nombres='Camila', apellidos='Rojas Mendez',
        fecha_nac=datetime.date(2003, 12, 3), genero='F',
        email='camila.rojas@estudiantes.edu.co',
        telefono='3195556677', ciudad='Medellín')

    # ── 6. DOCENTES ───────────────────────────────────────────
    doc1 = Docente.objects.create(
        persona=per_doc1, codigo='DOC001',
        departamento=dep_sistemas,
        titulo_maximo='Magíster en Ingeniería de Software',
        dedicacion='Tiempo completo')
    doc2 = Docente.objects.create(
        persona=per_doc2, codigo='DOC002',
        departamento=dep_basicas,
        titulo_maximo='Doctora en Matemáticas',
        dedicacion='Tiempo completo')
    doc3 = Docente.objects.create(
        persona=per_doc3, codigo='DOC003',
        departamento=dep_admin,
        titulo_maximo='Especialista en Gestión Empresarial',
        dedicacion='Cátedra')

    # ── 7. ESTUDIANTES ────────────────────────────────────────
    est1 = Estudiante.objects.create(
        persona=per_est1, codigo='EST2024001',
        fecha_ingreso=datetime.date(2024, 1, 22))
    est2 = Estudiante.objects.create(
        persona=per_est2, codigo='EST2024002',
        fecha_ingreso=datetime.date(2024, 1, 22))
    est3 = Estudiante.objects.create(
        persona=per_est3, codigo='EST2024003',
        fecha_ingreso=datetime.date(2024, 7, 22))
    est4 = Estudiante.objects.create(
        persona=per_est4, codigo='EST2023001',
        fecha_ingreso=datetime.date(2023, 1, 23))
    est5 = Estudiante.objects.create(
        persona=per_est5, codigo='EST2025001',
        fecha_ingreso=datetime.date(2025, 1, 20))

    # ── 8. PROGRAMAS ──────────────────────────────────────────
    prog_sistemas = Programa.objects.create(
        nombre='Ingeniería de Sistemas',
        codigo='PROG-IS-01',
        nivel_formacion='Pregrado',
        modalidad='Presencial',
        departamento=dep_sistemas,
        creditos_totales=160,
        duracion_semestres=10)
    prog_admin = Programa.objects.create(
        nombre='Administración de Empresas',
        codigo='PROG-AE-01',
        nivel_formacion='Pregrado',
        modalidad='Presencial',
        departamento=dep_admin,
        creditos_totales=150,
        duracion_semestres=10)
    prog_virtual = Programa.objects.create(
        nombre='Tecnología en Desarrollo de Software',
        codigo='PROG-IS-02',
        nivel_formacion='Tecnólogo',
        modalidad='Virtual',
        departamento=dep_sistemas,
        creditos_totales=96,
        duracion_semestres=6)

    # ── 9. CURSOS ─────────────────────────────────────────────
    cur_prog1 = Curso.objects.create(
        programa=prog_sistemas, departamento=dep_basicas,
        nombre='Cálculo Diferencial', codigo='CB-101',
        creditos=4, horas_semana=5, nivel_semestre=1)
    cur_prog2 = Curso.objects.create(
        programa=prog_sistemas, departamento=dep_sistemas,
        nombre='Fundamentos de Programación', codigo='IS-101',
        creditos=3, horas_semana=4, nivel_semestre=1)
    cur_prog3 = Curso.objects.create(
        programa=prog_sistemas, departamento=dep_sistemas,
        nombre='Estructuras de Datos', codigo='IS-201',
        creditos=3, horas_semana=4, nivel_semestre=3)
    cur_prog4 = Curso.objects.create(
        programa=prog_sistemas, departamento=dep_sistemas,
        nombre='Base de Datos I', codigo='IS-301',
        creditos=3, horas_semana=4, nivel_semestre=4)
    cur_prog5 = Curso.objects.create(
        programa=prog_admin, departamento=dep_admin,
        nombre='Fundamentos de Administración', codigo='AE-101',
        creditos=3, horas_semana=4, nivel_semestre=1)
    cur_prog6 = Curso.objects.create(
        programa=prog_virtual, departamento=dep_sistemas,
        nombre='Desarrollo Web', codigo='IS-401',
        creditos=3, horas_semana=4, nivel_semestre=4,
        electiva=True)

    # ── 10. AULAS ─────────────────────────────────────────────
    aula1 = Aula.objects.create(
        edificio=ed_a, tipo='Salón de clase',
        nombre='A-101', piso=1, capacidad=40)
    aula2 = Aula.objects.create(
        edificio=ed_a, tipo='Salón de clase',
        nombre='A-102', piso=1, capacidad=35)
    aula3 = Aula.objects.create(
        edificio=ed_b, tipo='Salón de clase',
        nombre='B-201', piso=2, capacidad=45)
    aula4 = Aula.objects.create(
        edificio=ed_c, tipo='Laboratorio de cómputo',
        nombre='C-LAB1', piso=1, capacidad=30)
    aula5 = Aula.objects.create(
        edificio=ed_c, tipo='Laboratorio de cómputo',
        nombre='C-LAB2', piso=1, capacidad=30)

    # ── 11. GRUPOS ────────────────────────────────────────────
    g1 = GrupoCurso.objects.create(
        curso=cur_prog1, docente=doc2, periodo=p_2025_2,
        modalidad='Presencial', nombre_grupo='A', cupo_maximo=35)
    g2 = GrupoCurso.objects.create(
        curso=cur_prog2, docente=doc1, periodo=p_2025_2,
        modalidad='Presencial', nombre_grupo='A', cupo_maximo=30)
    g3 = GrupoCurso.objects.create(
        curso=cur_prog3, docente=doc1, periodo=p_2025_2,
        modalidad='Presencial', nombre_grupo='A', cupo_maximo=30)
    g4 = GrupoCurso.objects.create(
        curso=cur_prog4, docente=doc1, periodo=p_2025_2,
        modalidad='Presencial', nombre_grupo='A', cupo_maximo=30)
    g5 = GrupoCurso.objects.create(
        curso=cur_prog5, docente=doc3, periodo=p_2025_2,
        modalidad='Presencial', nombre_grupo='A', cupo_maximo=40)
    g6 = GrupoCurso.objects.create(
        curso=cur_prog6, docente=doc1, periodo=p_2025_2,
        modalidad='Virtual', nombre_grupo='A', cupo_maximo=25)

    # ── 12. HORARIOS ──────────────────────────────────────────
    Horario.objects.create(grupo=g1, aula=aula1, dia='Lunes',    hora_inicio='07:00', hora_fin='09:00')
    Horario.objects.create(grupo=g1, aula=aula1, dia='Miércoles',hora_inicio='07:00', hora_fin='09:00')
    Horario.objects.create(grupo=g2, aula=aula4, dia='Lunes',    hora_inicio='09:00', hora_fin='11:00')
    Horario.objects.create(grupo=g2, aula=aula4, dia='Miércoles',hora_inicio='09:00', hora_fin='11:00')
    Horario.objects.create(grupo=g3, aula=aula4, dia='Martes',   hora_inicio='07:00', hora_fin='09:00')
    Horario.objects.create(grupo=g3, aula=aula4, dia='Jueves',   hora_inicio='07:00', hora_fin='09:00')
    Horario.objects.create(grupo=g4, aula=aula5, dia='Martes',   hora_inicio='09:00', hora_fin='11:00')
    Horario.objects.create(grupo=g4, aula=aula5, dia='Jueves',   hora_inicio='09:00', hora_fin='11:00')
    Horario.objects.create(grupo=g5, aula=aula2, dia='Viernes',  hora_inicio='07:00', hora_fin='09:00')
    Horario.objects.create(grupo=g5, aula=aula2, dia='Sábado',   hora_inicio='07:00', hora_fin='09:00')
    Horario.objects.create(grupo=g6, aula=aula3, dia='Sábado',   hora_inicio='09:00', hora_fin='11:00')

    # ── 13. MATRÍCULAS ────────────────────────────────────────
    mat1 = Matricula.objects.create(estudiante=est1, grupo=g1, periodo=p_2025_2, estado='Activa')
    mat2 = Matricula.objects.create(estudiante=est1, grupo=g2, periodo=p_2025_2, estado='Activa')
    mat3 = Matricula.objects.create(estudiante=est2, grupo=g1, periodo=p_2025_2, estado='Activa')
    mat4 = Matricula.objects.create(estudiante=est2, grupo=g3, periodo=p_2025_2, estado='Activa')
    mat5 = Matricula.objects.create(estudiante=est3, grupo=g2, periodo=p_2025_2, estado='Activa')
    mat6 = Matricula.objects.create(estudiante=est3, grupo=g4, periodo=p_2025_2, estado='Activa')
    mat7 = Matricula.objects.create(estudiante=est4, grupo=g4, periodo=p_2025_2, estado='Activa')
    mat8 = Matricula.objects.create(estudiante=est4, grupo=g5, periodo=p_2025_2, estado='Activa')
    mat9 = Matricula.objects.create(estudiante=est5, grupo=g5, periodo=p_2025_2, estado='Activa')
    mat10= Matricula.objects.create(estudiante=est5, grupo=g6, periodo=p_2025_2, estado='Activa')

    # Matrícula cancelada y finalizada de ejemplo
    Matricula.objects.create(
        estudiante=est1, grupo=g5, periodo=p_2024_1,
        estado='Finalizada', nota_final='3.80')
    Matricula.objects.create(
        estudiante=est2, grupo=g5, periodo=p_2024_2,
        estado='Cancelada')

    # ── 14. EVALUACIONES ──────────────────────────────────────
    # Grupo 1 – Cálculo Diferencial
    ev1_p1 = Evaluacion.objects.create(
        grupo=g1, tipo='Parcial', nombre='Primer Parcial',
        fecha_aplicacion=datetime.date(2025, 8, 20),
        porcentaje='30.00', nota_maxima='5.00')
    ev1_p2 = Evaluacion.objects.create(
        grupo=g1, tipo='Parcial', nombre='Segundo Parcial',
        fecha_aplicacion=datetime.date(2025, 9, 24),
        porcentaje='30.00', nota_maxima='5.00')
    ev1_fin = Evaluacion.objects.create(
        grupo=g1, tipo='Final', nombre='Examen Final',
        fecha_aplicacion=datetime.date(2025, 11, 12),
        porcentaje='40.00', nota_maxima='5.00')

    # Grupo 2 – Fundamentos de Programación
    ev2_q1 = Evaluacion.objects.create(
        grupo=g2, tipo='Quiz', nombre='Quiz 1 – Variables y tipos',
        fecha_aplicacion=datetime.date(2025, 8, 13),
        porcentaje='10.00', nota_maxima='5.00')
    ev2_p1 = Evaluacion.objects.create(
        grupo=g2, tipo='Parcial', nombre='Primer Parcial',
        fecha_aplicacion=datetime.date(2025, 9, 3),
        porcentaje='35.00', nota_maxima='5.00')
    ev2_proy = Evaluacion.objects.create(
        grupo=g2, tipo='Proyecto', nombre='Proyecto Final',
        fecha_aplicacion=datetime.date(2025, 11, 5),
        porcentaje='55.00', nota_maxima='5.00')

    # Grupo 4 – Base de Datos I
    ev4_p1 = Evaluacion.objects.create(
        grupo=g4, tipo='Parcial', nombre='Primer Parcial',
        fecha_aplicacion=datetime.date(2025, 8, 27),
        porcentaje='30.00', nota_maxima='5.00')
    ev4_taller = Evaluacion.objects.create(
        grupo=g4, tipo='Taller', nombre='Taller SQL',
        fecha_aplicacion=datetime.date(2025, 9, 17),
        porcentaje='20.00', nota_maxima='5.00')
    ev4_fin = Evaluacion.objects.create(
        grupo=g4, tipo='Final', nombre='Examen Final',
        fecha_aplicacion=datetime.date(2025, 11, 19),
        porcentaje='50.00', nota_maxima='5.00')

    # ── 15. NOTAS DE EVALUACIÓN ───────────────────────────────
    # Primer parcial Cálculo – est1 y est2
    NotaEvaluacion.objects.create(evaluacion=ev1_p1, estudiante=est1, nota='3.50')
    NotaEvaluacion.objects.create(evaluacion=ev1_p1, estudiante=est2, nota='4.20')

    # Segundo parcial Cálculo
    NotaEvaluacion.objects.create(evaluacion=ev1_p2, estudiante=est1, nota='3.80')
    NotaEvaluacion.objects.create(evaluacion=ev1_p2, estudiante=est2, nota='4.00')

    # Final Cálculo
    NotaEvaluacion.objects.create(evaluacion=ev1_fin, estudiante=est1, nota='4.10')
    NotaEvaluacion.objects.create(evaluacion=ev1_fin, estudiante=est2, nota='3.90')

    # Quiz Programación – est1 y est3
    NotaEvaluacion.objects.create(evaluacion=ev2_q1, estudiante=est1, nota='4.50')
    NotaEvaluacion.objects.create(evaluacion=ev2_q1, estudiante=est3, nota='3.00')

    # Parcial Programación
    NotaEvaluacion.objects.create(evaluacion=ev2_p1, estudiante=est1, nota='4.00')
    NotaEvaluacion.objects.create(evaluacion=ev2_p1, estudiante=est3, nota='3.50')

    # Proyecto Programación
    NotaEvaluacion.objects.create(evaluacion=ev2_proy, estudiante=est1, nota='4.80')
    NotaEvaluacion.objects.create(evaluacion=ev2_proy, estudiante=est3, nota='4.20')

    # Parcial Base de Datos – est3 y est4
    NotaEvaluacion.objects.create(evaluacion=ev4_p1, estudiante=est3, nota='3.20')
    NotaEvaluacion.objects.create(evaluacion=ev4_p1, estudiante=est4, nota='4.60')

    # Taller SQL – est4 ausente
    NotaEvaluacion.objects.create(evaluacion=ev4_taller, estudiante=est3, nota='4.00')
    NotaEvaluacion.objects.create(evaluacion=ev4_taller, estudiante=est4, ausente=True)

    # Final Base de Datos
    NotaEvaluacion.objects.create(evaluacion=ev4_fin, estudiante=est3, nota='3.70')
    NotaEvaluacion.objects.create(evaluacion=ev4_fin, estudiante=est4, nota='4.90')


def revertir_datos(apps, schema_editor):
    # El rollback elimina en orden inverso respetando FK
    for model_name in [
        'NotaEvaluacion', 'Evaluacion', 'Matricula', 'Horario',
        'GrupoCurso', 'Aula', 'Curso', 'Programa',
        'Estudiante', 'Docente', 'Persona',
        'PeriodoAcademico', 'Edificio', 'Departamento',
    ]:
        apps.get_model('api', model_name).objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insertar_datos, revertir_datos),
    ]
    