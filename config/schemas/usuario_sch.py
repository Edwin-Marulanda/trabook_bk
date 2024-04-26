from pydantic import BaseModel
from typing import Optional

class UsuarioBase (BaseModel):
    email: str
    nombres: str
    apellidos: str
    password: str
    grupo_id:int

class CrearUsuario(BaseModel):
    email: str
    nombres: str
    apellidos: str
    password: str
    grupo_id: int

class Usuario(UsuarioBase):
    id: int

    class config:
        orm_mode= True
