from django.db import models

# Create your models here.

class Curso(models.Model):
    """Modelo para representar un grado escolar"""
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=10, unique=True)  # Ejemplo: "11-A"
    
    def __str__(self):
        return self.codigo

class Estudiante(models.Model):
    """Modelo para representar un estudiante"""
    nombre_completo = models.CharField(max_length=255)
    documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    acudiente = models.CharField(max_length=255)
    curso = models.ForeignKey(Curso, related_name='estudiantes', on_delete=models.PROTECT)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre_completo} - {self.documento}"
