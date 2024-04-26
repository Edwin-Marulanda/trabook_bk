from sqlalchemy import String, Column, Integer, Date, Text, LargeBinary
from config.db import Base

class Articulo(Base):
    __tablename__="articulo"
    id= Column(Integer,primary_key=True, index=True, autoincrement=True)
    imagen= Column(Text,nullable=False)
    titulo = Column(String(100), nullable=False)
    fecha_publicacion = Column(Date, nullable=False)
    contenido= Column(Text, nullable=False)
