from ninja import ModelSchema
from .models import User

class UserInSchema(ModelSchema):
    class Meta:
        model = User
        fields = ['username','email_usuario','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido',]
        
        
class UserOutSchema(ModelSchema):
    class Meta:
        model = User
        fields = ['id_usuario','username','email_usuario','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido',]