from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from estructuras.vector import VectorPeliculas

app = FastAPI(title="Cine Santa Fe")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instanciamos la estructura del catálogo
catalogo_vector = VectorPeliculas()

@app.get("/api/peliculas")
def obtener_cartelera():
    """Ruta que devuelve el vector de películas al frontend"""
    return catalogo_vector.obtener_todas()

# Montamos las carpetas para que FastAPI pueda leer el HTML y CSS
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

# Cuando alguien entre a la URL principal, lo enviamos al inicio
@app.get("/")
def ruta_principal():
    return RedirectResponse(url="/templates/inicio.html")
