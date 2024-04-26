from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from config.db import SessionLocal
from typing import List
import config.schemas.ciudad_sch
import models.ciudad_model

ciudad = APIRouter(prefix="/ciudad")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# obtener los datos ciudades
@ciudad.get("/", response_model=List[config.schemas.ciudad_sch.Ciudad] )
async def fetch_ciudades(db:Session=Depends(get_db)):
    ciudades = db.query(models.ciudad_model.Ciudad).all()

    return ciudades

@ciudad.get("/{id_pais}", response_model=List[config.schemas.ciudad_sch.Ciudad])
async def fetch_ciudades_por_pais(id_pais: int, db: Session = Depends(get_db)):
    ciudades = db.query(models.ciudad_model.Ciudad).filter(models.ciudad_model.Ciudad.id_pais == id_pais).all()
    if not ciudades:
        raise HTTPException(status_code=404, detail="No se encontraron ciudades para el país")
    return ciudades