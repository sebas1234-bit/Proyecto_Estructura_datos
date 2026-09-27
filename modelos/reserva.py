# ============================================================
# CLASE RESERVA
# Une Persona + Pelicula + Asiento
# ============================================================

class Reserva:

    def __init__(self, persona, pelicula, asiento):
        self.persona = persona
        self.pelicula = pelicula
        self.asiento = asiento

    def mostrar_reserva(self):
        print("----------------------------------------")
        print("RESERVA")
        print("----------------------------------------")

        print(f"Persona: {self.persona.nombre}")
        print(f"Documento: {self.persona.documento}")
        print(f"Edad: {self.persona.edad}")

        print(f"Película: {self.pelicula.titulo}")

        print(
            f"Asiento: Fila {self.asiento.fila}, "
            f"Columna {self.asiento.columna}"
        )

        print("----------------------------------------")