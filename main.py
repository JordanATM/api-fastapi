from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar quién puede entrar
origins = [
    "http://localhost:5173",  # Tu app de React en desarrollo
    "https://tu-dominio-de-frontend.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hola desde FastAPI deployeado!"}

@app.get("/saludos")
def read_root():
    return {"message": "Saludos desde otra ruta!"}

