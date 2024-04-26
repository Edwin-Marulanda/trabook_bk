from fastapi import APIRouter
from sqlalchemy import text
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
import config.schemas.plan_sch
from config.db import SessionLocal
import models.plan_model

plan = APIRouter(prefix="/plan")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#routes
#-------------------------------------------------------

# obtener planes.
@plan.get("/planes")
async def obtener_planes(db:Session=Depends(get_db)):
    query = text("""
                       SELECT * from (
            select p.id, p.fecha_disponible, p.costo, p.dias, des.*
            from plan p join (
            SELECT d.id as destino_id, d.imagen, ci.nombre AS nombre_ciudad, p.nombre AS nombre_pais
            FROM destino d
            JOIN ciudad ci ON d.ciudad_id = ci.id 
            JOIN pais p ON ci.id_pais = p.id) des on p.destino_id = des.destino_id) dp 
            left join 
            (SELECT p.id, COALESCE(SUM(c.puntos) / COUNT(p.id), 0) AS puntuacion
                 FROM plan p
                 LEFT JOIN calificacion c ON p.id = c.plan_id
                 GROUP BY p.id) c ON dp.id = c.id
        """)
    planes = db.execute(query).fetchall()

    planes_list = []
    for plan in planes:
        planes_list.append({
            "id": plan.id,
            "destino_id": plan.destino_id,
            "costo": plan.costo,
            "imagen": plan.imagen,
            "fecha_disponible": plan.fecha_disponible,
            "dias": plan.dias,
            "ciudad": plan.nombre_ciudad,
            "pais": plan.nombre_pais,
            "puntuacion": plan.puntuacion
        })

    return planes_list


@plan.get("/ultimos")
async def fetch_ultimos_planes(db:Session=Depends(get_db)):
    query = text("""
                       SELECT * from (
            select p.id, p.fecha_disponible, p.costo, p.dias, des.*
            from plan p join (
            SELECT d.id as destino_id, d.imagen, ci.nombre AS nombre_ciudad, p.nombre AS nombre_pais
            FROM destino d
            JOIN ciudad ci ON d.ciudad_id = ci.id 
            JOIN pais p ON ci.id_pais = p.id) des on p.destino_id = des.destino_id) dp 
            left join 
            (SELECT p.id, COALESCE(SUM(c.puntos) / COUNT(p.id), 0) AS puntuacion
                 FROM plan p
                 LEFT JOIN calificacion c ON p.id = c.plan_id
                 GROUP BY p.id) c ON dp.id = c.id
            order by p.id desc
            LIMIT 6
        """)
    planes = db.execute(query).fetchall()

    planes_list = []
    for plan in planes:
        planes_list.append({
            "id": plan.id,
            "destino_id": plan.destino_id,
            "costo": plan.costo,
            "imagen": plan.imagen,
            "fecha_disponible": plan.fecha_disponible,
            "dias": plan.dias,
            "ciudad": plan.nombre_ciudad,
            "pais": plan.nombre_pais,
            "puntuacion":plan.puntuacion
        })

    return planes_list



@plan.post("/registrar-plan")
async def agregar_plan(plan: config.schemas.plan_sch.CrearPlan, db: Session = Depends(get_db)):
    db_plan = models.plan_model.Plan(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan