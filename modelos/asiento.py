# ============================================================
# CLASE ASIENTO
# ============================================================

class Asiento:

    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.estado = "Disponible"

    def ocupar(self):
        self.estado = "Ocupado"

    def liberar(self):
        self.estado = "Disponible"

    def esta_disponible(self):
        return self.estado == "Disponible"