# SIA Colegios - Microservicio de Gestión Académica

Este microservicio forma parte del Sistema de Información Académica (SIA) para colegios, proporcionando una API REST para la gestión de estudiantes y cursos.

## 🚀 Características Principales

- **API REST completa** para la gestión de estudiantes y cursos
- **Persistencia en PostgreSQL** con soporte para caracteres especiales
- **Contenerización con Docker** para facilitar el despliegue
- **Documentación de API integrada**
- **CRUD completo** para todas las entidades

## 💻 Tecnologías

- **Backend:**
  - Django 4.2.x
  - Django REST Framework 3.14.x
  - PostgreSQL 17
  - Gunicorn para producción

- **Contenerización:**
  - Docker
  - Docker Compose

## 🐳 Despliegue con Docker

La forma más rápida y recomendada para ejecutar este microservicio es utilizando Docker.

### Requisitos previos

- Docker y Docker Compose instalados

### Pasos para el despliegue

1. Clona este repositorio:
   ```bash
   git clone <repositorio>
   cd sia_colegios
   ```

2. Inicia los contenedores con Docker Compose:
   ```bash
   docker-compose up -d
   ```

3. La aplicación estará disponible en:
   - API REST: http://localhost:8000/api/
   - Administración: http://localhost:8000/admin/

### Arquitectura de contenedores

El proyecto está dividido en dos contenedores principales que se comunican a través de una red Docker:

- **web**: Aplicación Django que sirve la API REST
- **db**: Base de datos PostgreSQL con configuración para soporte de caracteres españoles

### Variables de entorno

Puedes personalizar la configuración mediante variables de entorno en el `docker-compose.yml`:

- `DB_HOST`: Host de la base de datos (por defecto: db)
- `DB_NAME`: Nombre de la base de datos (por defecto: sia_colegios)
- `DB_USER`: Usuario de la base de datos (por defecto: postgres)
- `DB_PASSWORD`: Contraseña de la base de datos (por defecto: postgres)
- `DB_PORT`: Puerto de la base de datos (por defecto: 5432)
- `LOAD_INITIAL_DATA`: Carga datos iniciales si se establece a 'true'

## 🔧 Instalación local (sin Docker)

Si prefieres desarrollar sin Docker, sigue estos pasos:

1. Crea y configura un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Configura PostgreSQL siguiendo las instrucciones en la sección "Configuración de PostgreSQL".

3. Aplica migraciones y crea un superusuario:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## 📊 Configuración de PostgreSQL

### Configuración rápida

Para configurar PostgreSQL para este proyecto:

1. Instala PostgreSQL 17 o superior

2. Crea la base de datos con el comando:
   ```
   createdb -U postgres -E UTF8 sia_colegios
   ```

3. Configura el archivo `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': 'sia_colegios',
           'USER': 'postgres',
           'PASSWORD': 'tu_contraseña',
           'HOST': 'localhost',
           'PORT': '5432',
           'OPTIONS': {
               'client_encoding': 'UTF8',
           },
       }
   }
   ```

### Solución a problemas comunes

- **Error de codificación**: Si encuentras errores con caracteres especiales, verifica que la base de datos esté creada con codificación UTF-8.
  
- **Error de autenticación**: Asegúrate de usar las credenciales correctas y verifica el método de autenticación en `pg_hba.conf`.

- **Problemas con idioma español**: Crea la base de datos con las opciones de collation adecuadas:
  ```
  CREATE DATABASE sia_colegios WITH ENCODING 'UTF8' LC_COLLATE 'es_CO.UTF-8' LC_CTYPE 'es_CO.UTF-8';
  ```

Para información más detallada sobre la configuración de PostgreSQL, consulta el archivo `README_POSTGRES.md`.

## 📚 API REST

### Endpoints principales

#### Cursos
- `GET /api/cursos/` - Listar todos los cursos
- `POST /api/cursos/` - Crear un nuevo curso
- `GET /api/cursos/{id}/` - Obtener detalles de un curso
- `PUT /api/cursos/{id}/` - Actualizar un curso
- `DELETE /api/cursos/{id}/` - Eliminar un curso
- `GET /api/cursos/{id}/estudiantes/` - Obtener estudiantes de un curso

#### Estudiantes
- `GET /api/estudiantes/` - Listar todos los estudiantes
- `POST /api/estudiantes/` - Crear un nuevo estudiante
- `GET /api/estudiantes/{id}/` - Obtener detalles de un estudiante
- `PUT /api/estudiantes/{id}/` - Actualizar un estudiante
- `DELETE /api/estudiantes/{id}/` - Eliminar un estudiante
- `GET /api/estudiantes/por_curso/?codigo=11-A` - Filtrar estudiantes por código de curso

### Funcionalidades adicionales

- **Búsqueda**: Usar parámetro `?search=` para buscar en todos los endpoints
- **Ordenamiento**: Usar parámetro `?ordering=campo` o `?ordering=-campo` (orden descendente)
- **Paginación**: Todas las respuestas de listado vienen paginadas con `count`, `next`, `previous` y `results`

Para una documentación completa de la API, consulta el archivo `API_DOCS.md` o utiliza la interfaz web navegable accediendo a http://localhost:8000/api/ desde un navegador.

## 🏗️ Estructura del Proyecto

```
sia_colegios/
│
├── gestion_estudiantes/   # Aplicación principal
│   ├── models.py          # Modelos de datos: Estudiante, Curso
│   ├── serializers.py     # Serializadores para la API REST
│   ├── views.py           # Vistas y endpoints de la API
│   └── urls.py            # Configuración de URLs 
│
├── sia_colegios/          # Configuración del proyecto Django
│   ├── settings.py        # Configuración del proyecto
│   └── urls.py            # URLs principales
│
├── Dockerfile             # Configuración para la creación de la imagen Docker
├── docker-compose.yml     # Configuración de servicios (web, PostgreSQL)
├── docker-entrypoint.sh   # Script de entrada para inicialización
├── init-db.sh             # Script para inicializar PostgreSQL
└── requirements.txt       # Dependencias del proyecto
```

## 📋 Funcionalidades implementadas

- **Gestión de Estudiantes**:
  - Registro completo con validación de datos
  - Asignación a cursos
  - Listado filtrable y ordenable

- **Gestión de Cursos**:
  - CRUD completo de cursos/grados
  - Consulta de estudiantes por curso
  - Validación de códigos únicos


## 📝 Licencia

Desarrollado como parte del proyecto de Arquitectura de Software 2025-1. 