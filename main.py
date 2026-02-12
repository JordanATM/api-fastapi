# main.py
from fastapi import FastAPI
# Configurar quién puede entrar
origins = [
    "http://localhost:5173",  # Tu app de React en desarrollo
    "https://tu-dominio-de-frontend.com", # (Opcional) Tu app cuando la subas a internet
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # O puedes poner ["*"] para permitir a TODO el mundo
    allow_credentials=True,
    allow_methods=["*"], # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"], # Permite todos los encabezados
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola desde FastAPI deployeado!"}
