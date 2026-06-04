# Gestion Administrativa

## Información general

- **Nombre del proyecto:** Gestion Administrativa
- **Autor:** Alejandro Zorro
- **Problema desarrollado:** Sistema de gestión académica para administrar periodos, departamentos, personas, estudiantes, docentes, programas, cursos, matrículas y procesos asociados mediante una API REST.

## Tecnologías utilizadas

- Python
- Django
- PostgreSQL
- Swagger
- Django REST Framework
- Simple JWT
- Django Filter

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/<usuario>/<repositorio>.git
cd GestionAdministrativa
```

2. Crear y activar el entorno virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

Dependencias instaladas:

- asgiref==3.11.1
- Django==6.0.6
- django-filter==25.2
- djangorestframework==3.17.1
- djangorestframework-simplejwt==5.5.1
- drf-yasg==1.21.15
- inflection==0.5.1
- packaging==26.2
- psycopg2-binary==2.9.12
- PyJWT==2.13.0
- python-decouple==3.8
- pytz==2026.2
- PyYAML==6.0.3
- sqlparse==0.5.5
- tzdata==2026.2
- uritemplate==4.2.0

4. Configurar variables de entorno:

- `DJANGO_SECRET_KEY`: clave secreta de Django.
- `DATABASE_URL`: URL de conexión a PostgreSQL, por ejemplo `postgres://user:password@localhost:5432/dbname`.
- `DEBUG`: `True` o `False`.

5. Ejecutar migraciones:

```bash
python manage.py migrate
```

## Ejecución

Iniciar el servidor localmente:

```bash
python run.py
```

Luego abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Endpoints principales

- `GET  /api/v1/periodos-academicos/`
- `GET  /api/v1/departamentos/`
- `GET  /api/v1/edificios/`
- `GET  /api/v1/personas/`
- `GET  /api/v1/estudiantes/`
- `GET  /api/v1/docentes/`
- `GET  /api/v1/programas/`
- `GET  /api/v1/cursos/`
- `GET  /api/v1/curso-prerrequisitos/`
- `GET  /api/v1/grupos-curso/`
- `GET  /api/v1/matriculas/`
- `GET  /api/v1/matricula-historial/`
- `GET  /api/v1/evaluaciones/`
- `GET  /api/v1/notas-evaluacion/`
- `GET  /api/v1/calificaciones-finales/`
- `GET  /api/v1/aulas/`
- `GET  /api/v1/horarios/`
- `GET  /api/v1/asistencia/`
- `GET  /api/v1/syllabus/`
- `GET  /api/v1/syllabus-unidades/`
- `GET  /api/v1/tutorias/`
- `GET  /api/v1/materiales-curso/`
- `GET  /api/v1/eventos-calendario/`
- `GET  /api/v1/becas-estudiante/`
- `GET  /api/v1/pagos/`
- `GET  /api/v1/homologaciones/`
- `GET  /api/v1/solicitudes-academicas/`
- `GET  /api/v1/sanciones/`
- `GET  /api/v1/usuarios/`
- `GET  /api/v1/auditoria/`

## Documentación Swagger

- `GET  /swagger/`

## Autenticación JWT

- `POST /api/token/` - Obtener par de tokens JWT.
