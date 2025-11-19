from django.db import models
# Create your models here.
class Venta(models.Model):
    
    class VentaMetodoPago(models.Choices):
        CONTADO='C','Contado'
        FINCANCIADO= 'F','Financiado'
        MIXTO = 'M','Mixto'
    
    id_venta= models.AutoField(primary_key=True)
    id_vehiculo= models.ForeignKey('vehicles.Vehiculo', on_delete=models.CASCADE, related_name='vehicles')
    id_cliente = models.ForeignKey('clientes.Cliente' , on_delete=models.CASCADE , related_name='clientes')
    id_usuario = models.ForeignKey('users.User', on_delete=models.CASCADE , related_name='users')
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_venta = models.DateField()
    metodo_pago= models.CharField(max_length=1, choices=VentaMetodoPago.choices)
    observaciones_venta = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)