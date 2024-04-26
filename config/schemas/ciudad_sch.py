from pydantic import BaseModel

class CiudadBase (BaseModel):
    nombre: str
    id_pais: int

class Ciudad(CiudadBase):
    id: int

    class config:
        orm_mode= True
