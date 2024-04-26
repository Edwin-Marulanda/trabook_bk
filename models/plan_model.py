from sqlalchemy import Column, Integer, Date, Text, Float,ForeignKey
from sqlalchemy.orm import relationship

from config.db import Base

class Plan(Base):
    __tablename__="plan"
    id= Column(Integer,primary_key=True, index=True, autoincrement=True)
    costo = Column(Float, nullable=False)
    dias = Column(Integer, nullable=False)
    fecha_disponible= Column(Date, nullable=False)
    destino_id = Column(Integer, ForeignKey('destino.id'), nullable=False)
