from fastapi import APIRouter
from passlib.context import CryptContext
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from config.db import SessionLocal
from typing import List
import config.schemas.usuario_sch
import models.usuario_model

usuario = APIRouter(prefix="/usuario")

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#routes
#-------------------------------------------------------

# obtener todos los usuarios de la base de datos.
@usuario.get("/listar-usuarios", response_model=List[config.schemas.usuario_sch.Usuario] )
async def fetchall_users(db:Session=Depends(get_db)):
    usuarios = db.query(models.usuario_model.Usuario).all()
    #print(usuarios)
    return usuarios


@usuario.post("/registrar-usuario", response_model=config.schemas.usuario_sch.Usuario)
async def agregar_usuario(usuario: config.schemas.usuario_sch.CrearUsuario, db: Session = Depends(get_db)):

    hashed_password = crypt_context.hash(usuario.password)

    usuario_bd = models.usuario_model.Usuario(
        nombres= usuario.nombres,
        apellidos = usuario.apellidos,
        email=usuario.email,
        password=hashed_password,
        grupo_id= usuario.grupo_id)

    db.add(usuario_bd)
    db.commit()
    db.refresh(usuario_bd)

    return usuario_bd