from sqlalchemy import String, Column, Integer
from config.db import Base

class Grupo(Base):
    __tablename__="grupo"
    id= Column(Integer,primary_key=True, index=True, autoincrement=True)
    tipo= Column(String(10), nullable=False)