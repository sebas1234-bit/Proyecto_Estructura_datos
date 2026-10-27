# ============================================================
# OPERACIONES REVERSIBLES (lo que se guarda en la pila)
#
# Idea clave: cada operación SABE cómo deshacerse a sí misma.
# Así, Cine no necesita if/else por tipo de operación.
#
# Para agregar un nuevo tipo de acción reversible en el futuro:
#   1. Crear una subclase de Operacion (con su nombre y su deshacer).
#   2. Hacer push de ella en la pila donde corresponda.
#   Nada más cambia.
# ============================================================

from datetime import datetime


class Operacion:
    """Clase base: guarda la reserva afectada y cuándo ocurrió."""

    nombre = "OPERACIÓN"

    def __init__(self, reserva):
        self.reserva = reserva
        self.fecha_hora = datetime.now()

    def mostrar(self):
        r = self.reserva

        print(f"[{self.fecha_hora.strftime('%d/%m/%Y %H:%M:%S')}] {self.nombre}")
        print(f"   Cliente: {r.persona.nombre} (Doc: {r.persona.documento})")
        print(f"   Película: {r.pelicula.titulo}")
        print(f"   Asiento: Fila {r.asiento.fila}, Columna {r.asiento.columna}")

    def deshacer(self, cine):
        """Revierte la operación. Devuelve (exito, mensaje)."""
        raise NotImplementedError("Cada operación debe implementar deshacer()")


class OperacionReserva(Operacion):
    """Se apila al confirmar una reserva. Deshacer = anular esa reserva."""

    nombre = "RESERVA"

    def deshacer(self, cine):
        self.reserva.asiento.liberar()
        cine.lista_reservas.eliminar(self.reserva)

        return True, "Reserva revertida: el asiento quedó disponible."


class OperacionCancelacion(Operacion):
    """Se apila al cancelar una reserva. Deshacer = reactivar esa reserva."""

    nombre = "CANCELACIÓN"

    def deshacer(self, cine):
        id_pelicula = self.reserva.pelicula.id_pelicula

        if cine.vector_peliculas.buscar_por_id(id_pelicula) is None:
            return False, "No se puede deshacer: la película ya fue eliminada."

        self.reserva.asiento.ocupar()
        cine.lista_reservas.agregar(self.reserva)
        cine.historial.eliminar_ultimo()

        return True, "Cancelación revertida: la reserva volvió a estar activa."