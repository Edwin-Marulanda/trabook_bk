from pydantic import BaseModel

class CrearGrupo(BaseModel):
    tipo: str

class Grupo(CrearGrupo):
    id: int

    class Config:
        orm_mode = True