from fastapi import APIRouter

from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from config.db import SessionLocal
from typing import List
import config.schemas.pais_sch
import models.pais_model

pais = APIRouter(prefix="/pais")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#routes
#-------------------------------------------------------

# obtener los datos de pais.
@pais.get("/", response_model=List[config.schemas.pais_sch.Pais] )
async def fetch_pais(db:Session=Depends(get_db)):
    paises = db.query(models.pais_model.Pais).all()

    return paises