from fastapi import APIRouter

from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from config.db import SessionLocal
from typing import List
import config.schemas.about_sch
import models.about_model

about = APIRouter(prefix="/about")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#routes
# obtener los datos about.
@about.get("/info", response_model=List[config.schemas.about_sch.About] )
async def fetch_about(db:Session=Depends(get_db)):
    abouts = db.query(models.about_model.About).all()

    return abouts