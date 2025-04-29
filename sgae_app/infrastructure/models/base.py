from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator

class Person(models.Model):
    first_name = models.CharField(
        'primer nombre',
        max_length=100,
    )
    second_name = models.CharField(
        'segundo nombre',
        max_length=100,
        blank=True,
        null=True,
    )
    first_lastname = models.CharField(
        'primer apellido',
        max_length=100,
    )
    second_lastname = models.CharField(
        'segundo apellido',
        max_length=100,
        blank=True,
        null=True,
    )
    id_card = models.CharField(
        'documento de identidad',
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(5)],
    )
    birthdate = models.DateField(
        'fecha de nacimiento',
    )
    place_of_birth = models.CharField(
        'lugar de nacimiento',
        max_length=100,
    )
    address = models.TextField(
        'dirección',
        max_length=255,
    )
    phone = models.CharField(
        'teléfono',
        max_length=20,
        validators=[MinLengthValidator(7)],
    )
    email = models.EmailField(
        'correo electrónico',
        max_length=100,
        unique=True,
        validators=[EmailValidator()],
    )

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['first_lastname', 'first_name']
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'first_lastname', 'birthdate'],
                name='unique_person'
            )
        ]

    def __str__(self):
        return f"{self.first_name} {self.first_lastname} ({self.id_card})"

    def get_full_name(self):
        names = [self.first_name]
        if self.second_name:
            names.append(self.second_name)
        
        lastnames = [self.first_lastname]
        if self.second_lastname:
            lastnames.append(self.second_lastname)
            
        return f"{' '.join(names)} {' '.join(lastnames)}"

    def get_short_name(self):
        return f"{self.first_name} {self.first_lastname}"