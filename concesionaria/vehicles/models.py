from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    
    class VehiculoTipo(models.TextChoices):
        NUEVO ='nuevo'
        USADO = 'usado'
        SEMINUEVO = 'seminuevo'
    
    class VehiculoTransmision(models.TextChoices):
        MANUAL = 'manual'
        AUTOMATICA= 'automatica'
        
    class VehiculoCombustible(models.TextChoices):
        DIESEL= 'diesel'
        NORMAL ='normal'
        
        
    vechiculo_id = models.AutoField()
    marca_vechiculo = models.CharField(max_length=50)
    modelo_vechiculo = models.CharField(max_length=50)
    anio_vheiculo = models.PositiveIntegerField()
    precio_vehiculo = models.DecimalField(max_digits=12, decimal_places=2)
    kilometraje_vehiculo= models.PositiveBigIntegerField(null=True , blank=True)
    tipo_vehiculo = models.CharField(max_length=10, choices=VehiculoTipo.choices)
    estado_vehiculo = models.CharField(max_length=50, null=False)
    chasis_vechiculo = models.CharField(max_length=100, unique=True, help_text='Numero de chapa del vehiculo')
    color_exterior_vehiculo = models.CharField(max_length=50, help_text='Color principal de la carrocería')
    color_interior_vehiculo = models.CharField(max_length=50, help_text='Color interior de la carrocería')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

 