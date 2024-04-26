from sqlalchemy import String, Column, Integer, Text
from sqlalchemy.orm import relationship
from config.db import Base

class Pais(Base):
    __tablename__="pais"
    id= Column(Integer,primary_key=True, index=True, autoincrement=True)
    nombre= Column(String(50),nullable=False)
    ciudades = relationship("Ciudad", back_populates="pais")
