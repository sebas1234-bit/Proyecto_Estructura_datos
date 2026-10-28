from estructuras.nodo import Nodo


class ColaEspera:

    def __init__(self):
        self.cabeza = None  # Primer cliente en la cola (frente)
        self.cola = None    # Último cliente en la cola (final)
        self.cantidad = 0

    def esta_vacia(self):
        return self.cabeza is None

    def add(self, persona, pelicula):
        """Añade un cliente al final de la cola (Enqueue)."""
        dato = {"persona": persona, "pelicula": pelicula}
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo

        self.cantidad += 1

    def poll(self):
        """Extrae y retorna el primer cliente de la cola (Dequeue)."""
        if self.esta_vacia():
            return None

        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente

        if self.cabeza is None:
            self.cola = None

        self.cantidad -= 1
        return dato

    def peek(self):
        """Consulta el primer cliente al frente de la cola sin removerlo."""
        if self.esta_vacia():
            return None
        return self.cabeza.dato

    def mostrar(self):
        if self.esta_vacia():
            print("\nLa lista de espera está vacía.")
            return

        print("\n=== LISTA DE ESPERA (COLA FIFO - PREESTRENOS) ===")
        actual = self.cabeza
        posicion = 1

        while actual is not None:
            persona = actual.dato["persona"]
            pelicula = actual.dato["pelicula"]
            print(
                f"{posicion}. {persona.nombre} (Doc: {persona.documento}) "
                f"-> Esperando preestreno: '{pelicula.titulo}'"
            )
            actual = actual.siguiente
            posicion += 1
