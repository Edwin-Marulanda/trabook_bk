from sqlalchemy import String, Column, Integer, ForeignKey
from config.db import Base

class Usuario(Base):
    __tablename__="usuario"
    id= Column(Integer,primary_key=True, index=True, autoincrement=True)
    nombres= Column(String(45),nullable=False)
    apellidos = Column(String(45), nullable=False)
    email= Column(String(100), nullable=False)
    password= Column(String(500),nullable=False)
    grupo_id =Column(Integer, ForeignKey('grupo.id'), nullable=False)
