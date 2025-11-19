from ninja import ModelSchema
from .models import Cliente

class ClienteInSchema(ModelSchema):
    model = Cliente
    fields = ['nombre_cliente','documento_cliente','email_cliente','direccion_cliente', 'created_at']
    
    
    
class ClienteOutSchema(ModelSchema):
    model = Cliente
    fields = ['id_cliente','nombre_cliente','documento_cliente','email_cliente','direccion_cliente', 'created_at']