from fastapi import FastAPI
from routes.usuario_route import usuario
from routes.about_route import about
from routes.articulo_route import articulo
from routes.destino_route import destino
from routes.pais_route import pais
from routes.ciudad_route import ciudad
from routes.plan_route import plan
from routes.grupo_route import grupo
from routes.login_route import logear
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(usuario)
app.include_router(about)
app.include_router(articulo)
app.include_router(destino)
app.include_router(pais)
app.include_router(ciudad)
app.include_router(plan)
app.include_router(grupo)
app.include_router(logear)

@app.get("/")
def prim():
    return "test"

