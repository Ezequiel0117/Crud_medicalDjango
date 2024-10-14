from django.db import models
from django.contrib.auth.models import User
# medico general, medico cardialogo, etc
class Clinic(models.Model):
    ruc = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Profession(models.Model):
    description = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.description

class Doctor(models.Model):
    SEX_CHOICES = ( ('M', 'Masculino'), ('F', 'Femenino'),)
    # Campo para el nombre del doctor (máximo 100 caracteres)
    first_name = models.CharField(max_length=100)
    
    # Campo para el apellido del doctor (máximo 100 caracteres)
    last_name = models.CharField(max_length=100)
    # medico cardialogo
    profession = models.ManyToManyField(Profession)
    clinic = models.ForeignKey(Clinic,on_delete=models.CASCADE, related_name='clinicas')
   
    sex = models.CharField(default="M",max_length=1, choices=SEX_CHOICES)
    
    # Campo para la fecha de nacimiento del doctor
    birth_date = models.DateField()
    
    # Campo para la dirección del doctor (máximo 255 caracteres)
    address = models.CharField(max_length=255)
    
    # Campo booleano que indica si el doctor está activo o no (True por defecto)
    is_active = models.BooleanField(default=True)
    # La clase Meta es una forma de definir configuraciones adicionales que no pertenecen a los campos de datos directamente, sino a aspectos más globales del modelo
    class Meta:
        # Nombre singular del modelo en la administración
        verbose_name = "Doctor"
        
        # Nombre plural del modelo en la administración
        verbose_name_plural = "Doctores"
        
        # Ordenar por apellido y nombre
        ordering = ['last_name', 'first_name']
    
    # Método para devolver la representación del doctor como cadena de texto
    def __str__(self):
        # Devuelve el nombre y apellido del doctor
        return f"{self.first_name} {self.last_name}"

class License(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20, unique=True)
    issued_date = models.DateField()

    def __str__(self):
        return f'License {self.license_number} - Doctor {self.doctor.first_name }'
    


class Medications(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        
    def __str__(self):
        return f'{self.description} - User:  {self.user.username}'
        
        