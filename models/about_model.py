from sqlalchemy import String, Column, Integer, Text
from config.db import Base

class About(Base):
    __tablename__="about"
    id= Column(Integer,primary_key=True, index=True, autoincrement=True)
    titulo= Column(String(45),nullable=False)
    contenido= Column(Text, nullable=False)
