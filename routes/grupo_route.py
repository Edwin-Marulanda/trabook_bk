from fastapi import APIRouter

from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from config.db import SessionLocal
from typing import List
import config.schemas.grupo_sch
import models.grupo_model

grupo = APIRouter(prefix="/grupo")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# obtener los grupos.
@grupo.get("/", response_model=List[config.schemas.grupo_sch.Grupo] )
async def fetch_grupo(db:Session=Depends(get_db)):
    grupos = db.query(models.grupo_model.Grupo).all()

    return grupos