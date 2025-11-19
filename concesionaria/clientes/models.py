from django.db import models

# Create your models here.
class Cliente(models.Model):
    
    
    class ClienteDocumentoTipo(models.Choices):
        DNI = "DNI", "Documento Nacional de Identidad"
        RUC = "RUC", "Registro Único de Contribuyente"
        PASSPORT = "PAS", "Pasaporte"
        
        
    id_cliente= models.AutoField(primary_key=True)
    nombre_cliente = models.TextField(max_length=100)
    documento_cliente = models.TextField(max_length=10, choices=ClienteDocumentoTipo.choices)
    email_cliente= models.TextField(max_length=100)
    direccion_cliente = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)