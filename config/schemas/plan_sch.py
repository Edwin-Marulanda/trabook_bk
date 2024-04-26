from datetime import datetime
from pydantic import BaseModel

class CrearPlan(BaseModel):
    costo:float
    dias:int
    fecha_disponible: datetime
    destino_id: int

class Destino(CrearPlan):
    id: int

    class Config:
        orm_mode = True
