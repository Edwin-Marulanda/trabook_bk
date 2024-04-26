from datetime import datetime
from pydantic import BaseModel

class CrearDestino(BaseModel):
    costo:float
    costo_descuento :float
    fecha_disponible: datetime
    imagen: str
    ciudad_id: int

class Destino(CrearDestino):
    id: int

    class Config:
        orm_mode = True
