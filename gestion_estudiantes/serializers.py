from rest_framework import serializers
from .models import Curso, Estudiante

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class CursoDetailSerializer(serializers.ModelSerializer):
    estudiantes = serializers.SerializerMethodField()
    
    class Meta:
        model = Curso
        fields = '__all__'
    
    def get_estudiantes(self, obj):
        # Optimizado: usar select_related para evitar N+1 queries
        # Usar un serializer simple para evitar recursión
        estudiantes = obj.estudiantes.all()
        return [
            {
                'id': est.id,
                'nombreCompleto': est.nombre_completo,
                'documento': est.documento,
                'fechaNacimiento': est.fecha_nacimiento,
                'acudiente': est.acudiente,
                'fechaRegistro': est.fecha_registro
            }
            for est in estudiantes
        ]

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'
    
    def validate_documento(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("El documento debe contener solo números.")
        return value
    
    def validate_fecha_nacimiento(self, value):
        from django.utils import timezone
        if value > timezone.now().date():
            raise serializers.ValidationError("La fecha de nacimiento no puede ser en el futuro.")
        return value
    
    def validate(self, data):
        # Validar que el curso exista
        curso = data.get('curso')
        if curso and not Curso.objects.filter(id=curso.id).exists():
            raise serializers.ValidationError({"curso": "El curso especificado no existe."})
        return data

class EstudianteDetailSerializer(serializers.ModelSerializer):
    # Optimizado: usar SerializerMethodField para evitar consultas adicionales
    # cuando los datos ya están precargados con select_related
    curso = serializers.SerializerMethodField()
    
    class Meta:
        model = Estudiante
        fields = '__all__'
    
    def get_curso(self, obj):
        # Si el curso ya está precargado (select_related), usar esos datos
        if hasattr(obj, '_prefetched_objects_cache') and 'curso' in obj._prefetched_objects_cache:
            curso = obj._prefetched_objects_cache['curso']
        else:
            # Fallback: hacer consulta individual si no está precargado
            curso = obj.curso
        
        if curso:
            return {
                'id': curso.id,
                'nombre': curso.nombre,
                'codigo': curso.codigo
            }
        return None 