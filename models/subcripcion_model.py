from sqlalchemy import String, Column, Integer, Text
from config.db import Base

class Subscripcion(Base):
    __tablename__="subcripcion"
    id= Column(Integer,primary_key=True, index=True, autoincrement=True)
    email= Column(String(45),nullable=False)
    #usuario= Column(, nullable=False)
