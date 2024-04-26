from sqlalchemy import Column, Integer, Date, Text, Float,ForeignKey
from sqlalchemy.orm import relationship

from config.db import Base

class Destino(Base):
    __tablename__="destino"
    id= Column(Integer,primary_key=True, index=True, autoincrement=True)
    costo = Column(Float, nullable=False)
    costo_descuento = Column(Float, nullable=False)
    fecha_disponible= Column(Date, nullable=False)
    ciudad_id = Column(Integer, ForeignKey('ciudad.id'), nullable=False)
    imagen= Column(Text,nullable=False)
