from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Ciudad(Base):
    __tablename__ = "ciudad"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(45), nullable=False)
    id_pais = Column(Integer, ForeignKey('pais.id'), nullable=False)
    pais = relationship("Pais", back_populates="ciudades")