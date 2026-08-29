class VectorPeliculas:
    def __init__(self):
        # Inicializamos el vector (lista en Python) simulando el catálogo
        self.catalogo = []
        self._cargar_peliculas_iniciales()

    def _cargar_peliculas_iniciales(self):
        # Agregamos 3 películas con su información básica
        self.catalogo = [
            {
                "id": 1,
                "titulo": "El Despertar de la Fuerza",
                "genero": "Ciencia Ficción",
                "duracion": "135 min",
                "imagen": "https://placehold.co/300x450/1a1a2e/e50914?text=Star+Wars"
            },
            {
                "id": 2,
                "titulo": "Misión Imposible",
                "genero": "Acción",
                "duracion": "147 min",
                "imagen": "https://placehold.co/300x450/1a1a2e/e50914?text=Accion"
            },
            {
                "id": 3,
                "titulo": "Intensamente 2",
                "genero": "Animación",
                "duracion": "96 min",
                "imagen": "https://placehold.co/300x450/1a1a2e/e50914?text=Animacion"
            }
        ]

    def obtener_todas(self):
        # Acceso directo al vector O(1)
        return self.catalogo