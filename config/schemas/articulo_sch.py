from datetime import datetime
from pydantic import BaseModel

class CrearArticulo(BaseModel):
    titulo: str
    contenido: str
    fecha_publicacion: datetime = datetime.now()
    imagen: str

class Articulo(CrearArticulo):
    id: int

    class Config:
        orm_mode = True

