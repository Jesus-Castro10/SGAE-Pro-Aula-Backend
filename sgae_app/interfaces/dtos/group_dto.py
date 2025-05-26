from rest_framework import serializers
from sgae_app.infrastructure.models.schedule import ScheduleModel
from sgae_app.domain.entities.group import Group, Shift
from enum import Enum

class ShiftField(serializers.Field):
    """Campo personalizado para manejar la enumeración Shift."""
    
    def to_representation(self, value):
        # Convertir la enumeración a su valor para la respuesta
        return value.value if value else None
    
    def to_internal_value(self, data):
        # Convertir el string de entrada a la enumeración correspondiente
        if not data:
            return None
            
        try:
            # Buscar la enumeración por su valor
            for shift in Shift:
                if shift.value.lower() == data.lower():
                    return shift
            # Si no se encuentra por valor, intentar por nombre
            return Shift[data.upper()]
        except (KeyError, AttributeError):
            raise serializers.ValidationError(
                f"Turno no válido. Opciones válidas: {', '.join([s.value for s in Shift])}"
            )

class GroupDTO(serializers.Serializer):
    """
    DTO para la serialización de grupos.
    Incluye validaciones y metadatos para el frontend.
    """
    id = serializers.IntegerField(read_only=True)
    
    name = serializers.CharField(
        max_length=10,
        help_text="Nombre corto del grupo (ej: '1A', '2B')",
        error_messages={
            'blank': 'El nombre del grupo es obligatorio',
            'max_length': 'El nombre no puede tener más de 10 caracteres'
        }
    )
    
    year = serializers.IntegerField(
        min_value=2000,
        max_value=2100,
        help_text='Año académico (ej: 2025)',
        error_messages={
            'required': 'El año es obligatorio',
            'min_value': 'El año debe ser mayor o igual a 2000',
            'max_value': 'El año no puede ser mayor a 2100'
        }
    )
    
    section = serializers.CharField(
        max_length=10, 
        required=False, 
        allow_blank=True,
        help_text='Sección del grupo (opcional)',
        error_messages={
            'max_length': 'La sección no puede tener más de 10 caracteres'
        }
    )
    
    shift = ShiftField(
        required=False,
        allow_null=True,
        help_text='Turno del grupo (Mañana o Tarde)',
        error_messages={
            'invalid_choice': 'Turno no válido. Opciones: Mañana, Tarde'
        }
    )
    
    registered_at = serializers.DateTimeField(
        read_only=True,
        help_text='Fecha de creación del registro'
    )
    
    schedule = serializers.PrimaryKeyRelatedField(
        queryset=ScheduleModel.objects.all(),
        required=False,
        allow_null=True,
        help_text='ID del horario asociado',
        error_messages={
            'does_not_exist': 'El horario especificado no existe'
        }
    )
    
    # Campos calculados para el frontend
    display_name = serializers.SerializerMethodField(
        help_text='Nombre completo del grupo para mostrar'
    )
    
    def get_display_name(self, obj):
        """Genera un nombre para mostrar en el frontend."""
        name_parts = [f"{obj.name}"]
        if obj.shift:
            name_parts.append(f"({obj.shift})")
        if obj.section:
            name_parts.append(f"- {obj.section}")
        return " ".join(name_parts)
    
    def validate_name(self, value):
        """Validación personalizada para el nombre."""
        # Eliminar espacios en blanco y convertir a mayúsculas
        value = value.strip().upper()
        # Validar formato (ej: 1A, 2B, etc.)
        if not value or not value[0].isdigit() or len(value) < 2 or not value[1:].isalpha():
            raise serializers.ValidationError("Formato de grupo inválido. Debe ser algo como '1A', '2B', etc.")
        return value