from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from estructuras.vector import VectorPeliculas
from estructuras.matriz import MatrizAsientos

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
sala_asientos = MatrizAsientos(filas=5, columnas=8)
sala_asientos.reservar(1, 3, "Ana")

@app.get("/api/peliculas")
def obtener_cartelera():
    """Ruta que devuelve el vector de películas al frontend"""
    return catalogo_vector.obtener_todas()

@app.get("/api/asientos")
def obtener_asientos():
    """Ruta que devuelve la matriz de asientos al frontend"""
    return sala_asientos.a_estructura_json()

# Montamos las carpetas para que FastAPI pueda leer el HTML y CSS
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

# Cuando alguien entre a la URL principal, lo enviamos al inicio
@app.get("/")
def ruta_principal():
    return RedirectResponse(url="/templates/inicio.html")
