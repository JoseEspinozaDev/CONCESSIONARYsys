from django.db import models

# Create your models here.
class User(models.Model):
    
    
    class UserRole(models.TextChoices):
        ADMIN= 'admin','admin'
        VENDEDOR = 'vendedor','vendedor'
        VISUALIZADOR = 'visualizador','visualizador'
        
        
    id_usuario = models.AutoField()
    username= models.TextField(max_length=100, unique=True)
    email_usuario=models.TextField(max_length=150, unique=True)
    primer_nombre = models.TextField(max_length=50)
    segundo_nombre = models.TextField(max_length=50)
    primer_apellido = models.TextField(max_length=50)
    segundo_apellido = models.TextField(max_length=50)
    pasword_hash = models.TextField(max_length=255)
    role_usuario = models.CharField(max_length=10,choices=UserRole.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)