from fastapi import APIRouter, HTTPException

from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from config.db import SessionLocal
from typing import List
import config.schemas.articulo_sch
import models.articulo_model

articulo = APIRouter(prefix="/articulo")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#routes
#-------------------------------------------------------

# obtener
@articulo.get("/listar-articulos", response_model=List[config.schemas.articulo_sch.Articulo] )
async def obtener_articulos(db:Session=Depends(get_db)):
    articulos = db.query(models.articulo_model.Articulo).all()
    articulos.reverse()
    return articulos

@articulo.get("/articulos-principal", response_model=List[config.schemas.articulo_sch.Articulo] )
async def obtener_articulos_oferta(db:Session=Depends(get_db)):
    articulos = db.query(models.articulo_model.Articulo).all()
    articulos.reverse()
    return articulos[:8]

@articulo.put("/editar-articulo/{articulo_id}", response_model=config.schemas.articulo_sch.Articulo)
async def editar_articulo(articulo_id: int, articulo: config.schemas.articulo_sch.Articulo,
        db: Session = Depends(get_db)):
        db_articulo = db.query(models.articulo_model.Articulo).filter(
        models.articulo_model.Articulo.id == articulo_id).first()

        if not db_articulo:
            raise HTTPException(status_code=404, detail="Artículo no encontrado")

        db.query(models.articulo_model.Articulo).filter(models.articulo_model.Articulo.id == articulo_id).update({
            "imagen": articulo.imagen,
            "titulo": articulo.titulo,
            "contenido": articulo.contenido
        })
        db.commit()

        return articulo

@articulo.post("/registrar-articulo")
async def agregar_articulo(articulo: config.schemas.articulo_sch.CrearArticulo, db: Session = Depends(get_db)):
    db_articulo = models.articulo_model.Articulo(**articulo.dict())
    db.add(db_articulo)
    db.commit()
    db.refresh(db_articulo)
    return db_articulo


@articulo.delete("/eliminar-articulo/{articulo_id}")
async def eliminar_articulo(articulo_id: int, db: Session = Depends(get_db)):
    db_articulo = db.query(models.articulo_model.Articulo).filter(models.articulo_model.Articulo.id == articulo_id).first()
    if not db_articulo:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    db.delete(db_articulo)
    db.commit()
    return {"mensaje": "Artículo eliminado correctamente"}