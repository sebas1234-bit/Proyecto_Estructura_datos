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

catalogo_vector = VectorPeliculas()
sala_asientos = MatrizAsientos(filas=5, columnas=8)
sala_asientos.reservar(1, 3, "Ana")


class ReservaAsiento(BaseModel):
    fila: int
    columna: int
    usuario: str


class GestorConexiones:
    """Administra los WebSockets conectados y transmite (broadcast)
    los cambios de la matriz de asientos a todos los conectados."""

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
    """Reserva un asiento y avisa por WebSocket a todos los conectados."""
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
            await websocket.receive_text()  # mantiene la conexión viva
    except WebSocketDisconnect:
        gestor.desconectar(websocket)


app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")


@app.get("/")
def ruta_principal():
    return RedirectResponse(url="/templates/inicio.html")
