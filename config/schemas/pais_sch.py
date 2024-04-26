from pydantic import BaseModel

class PaisBase (BaseModel):
    nombre: str

class Pais(PaisBase):
    id: int

    class config:
        orm_mode= True
