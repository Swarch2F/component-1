import os
import django
import datetime
import random

# Configurar entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sia_colegios.settings')
django.setup()

# Importar modelos después de configurar el entorno
from gestion_estudiantes.models import Curso, Estudiante

def crear_cursos():
    """Crear cursos de ejemplo"""
    cursos_data = [
        {'nombre': 'Primero A', 'codigo': '1-A'},
        {'nombre': 'Primero B', 'codigo': '1-B'},
        {'nombre': 'Primero C', 'codigo': '1-C'},
        {'nombre': 'Segundo A', 'codigo': '2-A'},
        {'nombre': 'Segundo B', 'codigo': '2-B'},
        {'nombre': 'Segundo C', 'codigo': '2-C'},
        {'nombre': 'Tercero A', 'codigo': '3-A'},
        {'nombre': 'Tercero B', 'codigo': '3-B'},
        {'nombre': 'Tercero C', 'codigo': '3-C'},
        {'nombre': 'Cuarto A', 'codigo': '4-A'},
        {'nombre': 'Quinto A', 'codigo': '5-A'},
        {'nombre': 'Sexto A', 'codigo': '6-A'},
        {'nombre': 'Séptimo A', 'codigo': '7-A'},
        {'nombre': 'Octavo A', 'codigo': '8-A'},
        {'nombre': 'Noveno A', 'codigo': '9-A'},
        {'nombre': 'Décimo A', 'codigo': '10-A'},
        {'nombre': 'Once A', 'codigo': '11-A'},
        {'nombre': 'Once B', 'codigo': '11-B'},
    ]
    
    cursos_creados = []
    for curso_data in cursos_data:
        curso, created = Curso.objects.get_or_create(**curso_data)
        if created:
            print(f"Curso creado: {curso.codigo} - {curso.nombre}")
        else:
            print(f"Curso ya existente: {curso.codigo} - {curso.nombre}")
        cursos_creados.append(curso)
    
    return cursos_creados

def crear_estudiantes(cursos):
    """Crear estudiantes de ejemplo"""
    if not cursos:
        print("No hay cursos disponibles para crear estudiantes")
        return
    
    # Nombres y apellidos para generar combinaciones aleatorias
    nombres = [
        'Ana', 'Juan', 'Sofía', 'Miguel', 'Laura', 'Carlos', 'Valentina', 'Andrés', 
        'María', 'José', 'Isabella', 'Santiago', 'Camila', 'Daniel', 'Gabriela', 'Alejandro',
        'Valeria', 'Mateo', 'Lucía', 'Samuel', 'Mariana', 'Nicolás', 'Paula', 'David'
    ]
    
    apellidos = [
        'García', 'Rodríguez', 'Martínez', 'López', 'González', 'Pérez', 'Sánchez', 'Ramírez',
        'Torres', 'Flores', 'Rivera', 'Gómez', 'Díaz', 'Reyes', 'Cruz', 'Morales',
        'Herrera', 'Ortiz', 'Vargas', 'Mendoza', 'Castillo', 'Rojas', 'Romero', 'Álvarez'
    ]
    
    # Estudiantes existentes
    estudiantes_data = [
        {
            'nombre_completo': 'Ana María López',
            'documento': '1001234567',
            'fecha_nacimiento': datetime.date(2010, 5, 15),
            'acudiente': 'María Rodríguez',
            'curso': cursos[0]  # Primero A
        },
        {
            'nombre_completo': 'Juan Carlos Pérez',
            'documento': '1001234568',
            'fecha_nacimiento': datetime.date(2009, 8, 21),
            'acudiente': 'Carlos Pérez',
            'curso': cursos[4]  # Segundo B
        },
        {
            'nombre_completo': 'Sofía Alejandra Martínez',
            'documento': '1001234569',
            'fecha_nacimiento': datetime.date(2008, 3, 10),
            'acudiente': 'Alejandra Martínez',
            'curso': cursos[8]  # Tercero C
        },
        {
            'nombre_completo': 'Miguel Ángel Torres',
            'documento': '1001234570',
            'fecha_nacimiento': datetime.date(2002, 9, 5),
            'acudiente': 'Ángela Torres',
            'curso': cursos[14]  # Noveno A
        },
        {
            'nombre_completo': 'Laura Valentina Gómez',
            'documento': '1001234571',
            'fecha_nacimiento': datetime.date(2000, 2, 14),
            'acudiente': 'Valentina Gómez',
            'curso': cursos[16]  # Once A
        },
        {
            'nombre_completo': 'Carlos Eduardo Sánchez',
            'documento': '1001234572',
            'fecha_nacimiento': datetime.date(2000, 7, 30),
            'acudiente': 'Eduardo Sánchez',
            'curso': cursos[16]  # Once A
        }
    ]
    
    # Generar 30 estudiantes adicionales aleatoriamente
    for i in range(1, 31):
        nombre = random.choice(nombres)
        apellido1 = random.choice(apellidos)
        apellido2 = random.choice(apellidos)
        nombre_completo = f"{nombre} {apellido1} {apellido2}"
        
        # Generar documento único
        documento = f"10012345{72 + i}"
        
        # Fecha nacimiento aleatoria entre 2000 y 2015
        year = random.randint(2000, 2015)
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # Limitado a 28 para evitar problemas con febrero
        fecha_nacimiento = datetime.date(year, month, day)
        
        # Asignar acudiente
        acudiente = f"{random.choice(nombres)} {random.choice(apellidos)}"
        
        # Asignar curso según la edad
        edad = 2025 - year
        if edad <= 7:
            curso_index = random.randint(0, 2)  # Primero
        elif edad <= 8:
            curso_index = random.randint(3, 5)  # Segundo
        elif edad <= 9:
            curso_index = random.randint(6, 8)  # Tercero
        elif edad <= 10:
            curso_index = 9  # Cuarto
        elif edad <= 11:
            curso_index = 10  # Quinto
        elif edad <= 12:
            curso_index = 11  # Sexto
        elif edad <= 13:
            curso_index = 12  # Séptimo
        elif edad <= 14:
            curso_index = 13  # Octavo
        elif edad <= 15:
            curso_index = 14  # Noveno
        elif edad <= 16:
            curso_index = 15  # Décimo
        else:
            curso_index = random.choice([16, 17])  # Once
            
        curso = cursos[min(curso_index, len(cursos) - 1)]  # Evitar índice fuera de rango
        
        estudiantes_data.append({
            'nombre_completo': nombre_completo,
            'documento': documento,
            'fecha_nacimiento': fecha_nacimiento,
            'acudiente': acudiente,
            'curso': curso
        })
    
    for estudiante_data in estudiantes_data:
        try:
            estudiante, created = Estudiante.objects.get_or_create(
                documento=estudiante_data['documento'],
                defaults=estudiante_data
            )
            
            if created:
                print(f"Estudiante creado: {estudiante.nombre_completo} - Curso: {estudiante.curso.codigo}")
            else:
                print(f"Estudiante ya existente: {estudiante.nombre_completo}")
        except Exception as e:
            print(f"Error al crear estudiante {estudiante_data['nombre_completo']}: {e}")

def estadisticas():
    """Mostrar estadísticas de los datos cargados"""
    total_cursos = Curso.objects.count()
    total_estudiantes = Estudiante.objects.count()
    
    print("\n--- ESTADÍSTICAS DE DATOS ---")
    print(f"Total de cursos: {total_cursos}")
    print(f"Total de estudiantes: {total_estudiantes}")
    print("\nEstudiantes por curso:")
    
    for curso in Curso.objects.all().order_by('codigo'):
        num_estudiantes = Estudiante.objects.filter(curso=curso).count()
        print(f"  {curso.codigo} - {curso.nombre}: {num_estudiantes} estudiantes")

if __name__ == '__main__':
    print("Creando datos de prueba para el SIA Colegios...")
    cursos = crear_cursos()
    crear_estudiantes(cursos)
    estadisticas()
    print("Proceso completado.") 