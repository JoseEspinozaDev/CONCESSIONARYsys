from ninja import ModelSchema
from .models import Vehiculo

class VehicleInSchema(ModelSchema):
    class Meta:
        model = Vehiculo
        fields = ['marca_vechiculo']