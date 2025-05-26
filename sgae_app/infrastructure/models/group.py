from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from sgae_app.domain.entities.group import Group, Shift

class GroupModel(models.Model):
    """
    Modelo de base de datos para los grupos académicos.
    """
    # Usamos los valores de la enumeración Shift
    SHIFT_CHOICES = [
        (shift.value, shift.value) for shift in Shift
    ]
    
    id = models.AutoField(primary_key=True, verbose_name='ID')
    
    name = models.CharField(
        max_length=10,
        verbose_name='Nombre del grupo',
        help_text='Nombre corto del grupo (ej: 1A, 2B)'
    )
    
    year = models.PositiveIntegerField(
        verbose_name='Año académico',
        validators=[
            MinValueValidator(2000, 'El año debe ser mayor o igual a 2000'),
            MaxValueValidator(2100, 'El año no puede ser mayor a 2100')
        ],
        help_text='Año académico (ej: 2025)'
    )
    
    section = models.CharField(
        max_length=10,
        verbose_name='Sección',
        blank=True,
        null=True,
        help_text='Sección del grupo (opcional)'
    )
    
    shift = models.CharField(
        max_length=20,  # Aumentado para acomodar valores más largos
        choices=SHIFT_CHOICES,
        verbose_name='Turno',
        blank=True,
        null=True,
        help_text='Turno en el que se imparte el grupo (Mañana o Tarde)'
    )
    
    registered_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de registro'
    )
    
    schedule = models.ForeignKey(
        'ScheduleModel',
        on_delete=models.SET_NULL,
        related_name='groups',
        verbose_name='Horario',
        null=True,
        blank=True,
        help_text='Horario asociado al grupo'
    )

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['year', 'name', 'section']
        unique_together = ('name', 'year', 'section')
        indexes = [
            models.Index(fields=['year', 'name']),
            models.Index(fields=['shift']),
        ]

    def __str__(self):
        """Representación legible del grupo."""
        parts = [f"{self.name} - {self.year}"]
        if self.shift:
            parts.append(f"({self.get_shift_display()})")
        if self.section:
            parts.append(f"Sección {self.section}")
        return " ".join(parts)
    
    def to_domain(self):
        """Convierte el modelo a entidad de dominio."""
        return Group(
            id=self.id,
            name=self.name,
            year=self.year,
            section=self.section,
            shift=self.shift,
            registered_at=self.registered_at,
            schedule=self.schedule
        )

    @classmethod
    def from_domain(cls, group):
        """Crea un modelo a partir de una entidad de dominio."""
        return cls(
            id=group.id,
            name=group.name,
            year=group.year,
            section=group.section,
            shift=group.shift,
            registered_at=group.registered_at,
            schedule=group.schedule
        )
        
    def clean(self):
        """Validaciones adicionales del modelo."""
        super().clean()
        # Validar el formato del nombre (ej: 1A, 2B, etc.)
        if self.name:
            self.name = self.name.strip().upper()
            if not (self.name and self.name[0].isdigit() and len(self.name) >= 2 and self.name[1:].isalpha()):
                raise ValueError("Formato de grupo inválido. Debe ser algo como '1A', '2B', etc.")
    
    def save(self, *args, **kwargs):
        """Sobrescribes save para incluir validaciones."""
        self.clean()
        super().save(*args, **kwargs)