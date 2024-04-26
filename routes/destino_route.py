from fastapi import APIRouter
from sqlalchemy import text
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
import config.schemas.destino_sch
from config.db import SessionLocal
import models.destino_model

destino = APIRouter(prefix="/destino")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# obtener los datos de destino.
@destino.get("/destinos")
async def fetch_destinos(db:Session=Depends(get_db)):
    query = text("""
            SELECT d.id, d.costo, d.costo_descuento, d.imagen, d.fecha_disponible, COALESCE(c.puntuacion, 0) AS puntos,
                   ci.nombre AS nombre_ciudad, p.nombre AS nombre_pais
            FROM destino d
            LEFT JOIN 
                (SELECT d.id, COALESCE(SUM(c.puntos) / COUNT(d.id), 0) AS puntuacion
                 FROM destino d
                 LEFT JOIN calificacion c ON d.id = c.destino_id
                 GROUP BY d.id
                 ) c ON d.id = c.id
            JOIN ciudad ci ON d.ciudad_id = ci.id 
            JOIN pais p ON ci.id_pais = p.id
        """)
    destinos = db.execute(query).fetchall()

    destinos_list = []
    for destino in destinos:
        destinos_list.append({
            "destino_id": destino.id,
            "costo": destino.costo,
            "costo_descuento": destino.costo_descuento,
            "imagen": destino.imagen,
            "fecha_disponible": destino.fecha_disponible,
            "puntos": destino.puntos,
            "ciudad": destino.nombre_ciudad,
            "pais": destino.nombre_pais
        })

    return destinos_list

# obtener destinos ofertas
@destino.get("/ofertas")
async def fetch_destinos_oferta(db:Session=Depends(get_db)):
    query = text("""
            SELECT d.id, d.costo, d.costo_descuento, d.imagen, d.fecha_disponible, COALESCE(c.puntuacion, 0) AS puntos,
                   ci.nombre AS nombre_ciudad, p.nombre AS nombre_pais
            FROM destino d
            LEFT JOIN 
                (SELECT d.id, COALESCE(SUM(c.puntos) / COUNT(d.id), 0) AS puntuacion
                 FROM destino d
                 LEFT JOIN calificacion c ON d.id = c.destino_id
                 GROUP BY d.id) c ON d.id = c.id
            JOIN ciudad ci ON d.ciudad_id = ci.id 
            JOIN pais p ON ci.id_pais = p.id
            WHERE d.costo>d.costo_descuento
            order by d.id desc
        """)
    destinos = db.execute(query).fetchall()

    destinos_list = []
    for destino in destinos:
        destinos_list.append({
            "destino_id": destino.id,
            "costo": destino.costo,
            "costo_descuento": destino.costo_descuento,
            "imagen": destino.imagen,
            "fecha_disponible": destino.fecha_disponible,
            "puntos": destino.puntos,
            "ciudad": destino.nombre_ciudad,
            "pais": destino.nombre_pais
        })

    return destinos_list



@destino.post("/registrar-destino")
async def agregar_destino(destino: config.schemas.destino_sch.CrearDestino, db: Session = Depends(get_db)):
    db_destino = models.destino_model.Destino(**destino.dict())
    db.add(db_destino)
    db.commit()
    db.refresh(db_destino)
    return db_destino