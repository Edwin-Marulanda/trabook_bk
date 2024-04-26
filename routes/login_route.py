from fastapi import APIRouter
from passlib.context import CryptContext
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
import config.schemas.login_sch
from config.db import SessionLocal
import models.usuario_model

logear = APIRouter(prefix="/login")

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def verify_password(password, hashed_password):
    return crypt_context.verify(password, hashed_password)

def get_usuario(email: str,bd):
    return bd.query(models.usuario_model.Usuario).filter(models.usuario_model.Usuario.email == email).first()

def autenticar_usuario(email: str, password: str,bd):
    usuario = get_usuario(email,bd)
    if not usuario:
        return False
    if not verify_password(password, usuario.password):
        return False
    return usuario

@logear.post("/")
async def login(dataLogin: config.schemas.login_sch.Login, db: Session = Depends(get_db)):
    usuario = autenticar_usuario(dataLogin.email, dataLogin.password, db)
    if not usuario:
        return {"error": "Invalid credentials"}
    # Aquí generarías un token JWT o realizarías alguna otra acción de autenticación
    return usuario