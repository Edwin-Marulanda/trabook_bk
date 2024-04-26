from fastapi import APIRouter

from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from config.db import SessionLocal
from typing import List
import config.schemas.articulo_sch
import models.articulo_model

subscripcion = APIRouter(prefix="/subs")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#routes
#-------------------------------------------------------

#@subscripcion.post("/subscripcion")
#async def registrar_subscripcion(sub: config.schemas.articulo_sch.CrearArticulo, db: Session = Depends(get_db)):
