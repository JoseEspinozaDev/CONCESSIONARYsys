from ninja import ModelSchema
from .models import Vehiculo

class VehicleInSchema(ModelSchema):
    class Meta:
        model = Vehiculo
        fields = ['marca_vechiculo','modelo_vechiculo','anio_vheiculo','precio_vehiculo','kilometraje_vehiculo','tipo_vehiculo','estado_vehiculo','chasis_vechiculo','color_exterior_vehiculo','color_interior_vehiculo']
        
class VehicleOutSchema(ModelSchema):
    class Meta:
        model = Vehiculo
        fields =  ['vechiculo_id','marca_vechiculo','modelo_vechiculo','anio_vheiculo','precio_vehiculo','kilometraje_vehiculo','tipo_vehiculo','estado_vehiculo','chasis_vechiculo','color_exterior_vehiculo','color_interior_vehiculo']
        
        