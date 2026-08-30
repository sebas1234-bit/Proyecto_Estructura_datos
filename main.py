from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Dict, List
from estructuras.vector import VectorPeliculas
from estructuras.matriz import MatrizAsientos

app = FastAPI(title="Cine Santa Fe")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicialización de las estructuras de datos
catalogo_vector = VectorPeliculas()
sala_asientos = MatrizAsientos(filas=5, columnas=8)
sala_asientos.reservar(1, 3, "Ana")

# --- SISTEMA DE AUTENTICACIÓN TEMPORAL EN MEMORIA ---
usuarios_db = {}

class Usuario(BaseModel):
    correo: str
    contrasena: str

@app.post("/api/registro")
async def registrar_usuario(usuario: Usuario):
    if usuario.correo in usuarios_db:
        return {"mensaje": "El usuario ya existe. Intenta iniciar sesión.", "exito": False}
    usuarios_db[usuario.correo] = usuario.contrasena
    print("--- BASE DE DATOS ACTUALIZADA ---")
    print(usuarios_db)
    print("---------------------------------")
    return {"mensaje": "Registro exitoso. Ahora puedes iniciar sesión.", "exito": True}

@app.post("/api/login")
async def login_usuario(usuario: Usuario):
    if usuario.correo in usuarios_db and usuarios_db[usuario.correo] == usuario.contrasena:
        return {"mensaje": "¡Bienvenido a Cine Santa Fe!", "exito": True}
    return {"mensaje": "Correo o contraseña incorrectos.", "exito": False}

# --- GESTIÓN DE ASIENTOS Y WEBSOCKETS ---
class ReservaAsiento(BaseModel):
    fila: int
    columna: int
    usuario: str

class GestorConexiones:
    def __init__(self):
        self.conexiones: List[WebSocket] = []

    async def conectar(self, websocket: WebSocket):
        await websocket.accept()
        self.conexiones.append(websocket)

    def desconectar(self, websocket: WebSocket):
        if websocket in self.conexiones:
            self.conexiones.remove(websocket)

    async def difundir(self, mensaje: dict):
        for conexion in self.conexiones:
            await conexion.send_json(mensaje)

gestor = GestorConexiones()

@app.get("/api/peliculas")
def obtener_cartelera():
    return catalogo_vector.obtener_todas()

@app.get("/api/asientos")
def obtener_asientos():
    return sala_asientos.a_estructura_json()

@app.post("/api/asientos/reservar")
async def reservar_asiento(reserva: ReservaAsiento):
    exito = sala_asientos.reservar(reserva.fila, reserva.columna, reserva.usuario)
    if exito:
        await gestor.difundir({
            "fila": reserva.fila,
            "columna": reserva.columna,
            "ocupado_por": reserva.usuario,
        })
    return {"exito": exito}

@app.websocket("/ws/asientos")
async def websocket_asientos(websocket: WebSocket):
    await gestor.conectar(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        gestor.desconectar(websocket)

# Configuración de archivos estáticos y rutas
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

@app.get("/")
def ruta_principal():
    return RedirectResponse(url="/templates/inicio.html")
