from pydantic import BaseModel
from typing import Optional

class AboutBase (BaseModel):
    titulo: str
    contenido: str

class About(AboutBase):
    id: int

    class config:
        orm_mode= True
