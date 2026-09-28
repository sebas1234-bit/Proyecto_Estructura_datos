# ============================================================
# CLASE CINE
# Coordina todas las estructuras del sistema
# ============================================================

from modelos.persona import Persona
from modelos.reserva import Reserva

from estructuras.vector_peliculas import VectorPeliculas
from estructuras.matriz_asientos import MatrizAsientos
from estructuras.lista_simple_reservas import ListaSimpleReservas
from estructuras.lista_doble_historial import ListaDobleHistorial

from modelos.pelicula import Pelicula


class Cine:

    def __init__(self):

        self.vector_peliculas = VectorPeliculas()

        self.matriz_asientos = MatrizAsientos()

        self.lista_reservas = ListaSimpleReservas()

        self.historial = ListaDobleHistorial()

        self.siguiente_id_pelicula = 1


    # ========================================================
    # AGREGAR PELICULA  (Juan José)
    # ========================================================

    def agregar_pelicula(self):

        print("\n========== AGREGAR PELÍCULA ==========")

        titulo = input("Título: ").strip()

        while titulo == "":
            print("El título no puede estar vacío.")
            titulo = input("Título: ").strip()

        genero = input("Género: ").strip()

        while genero == "":
            print("El género no puede estar vacío.")
            genero = input("Género: ").strip()

        while True:

            try:

                duracion = int(
                    input("Duración en minutos: ")
                )

                if duracion <= 0:
                    print("La duración debe ser mayor que 0.")
                    continue

                break

            except ValueError:
                print("Ingrese un número válido.")

        pelicula = Pelicula(
            self.siguiente_id_pelicula,
            titulo,
            genero,
            duracion
        )

        self.vector_peliculas.agregar(pelicula)

        print("\nPelícula agregada correctamente.")
        print(f"ID asignado: {self.siguiente_id_pelicula}")

        self.siguiente_id_pelicula += 1


    # ========================================================
    # MOSTRAR PELICULAS  (Juan José)
    # ========================================================

    def mostrar_peliculas(self):

        print("\n========== CARTELERA ==========")

        peliculas = self.vector_peliculas.obtener_todas()

        if len(peliculas) == 0:
            print("No hay películas registradas.")
            return

        for pelicula in peliculas:

            pelicula.mostrar_informacion()
            print("----------------------------------------")


    # ========================================================
    # RESERVAR  (Juan José)
    # ========================================================

    def reservar(self):

        print("\n========== REALIZAR RESERVA ==========")

        peliculas = self.vector_peliculas.obtener_todas()

        if len(peliculas) == 0:

            print("No hay películas disponibles.")
            return

        # ----------------------------------------------------
        # MOSTRAR PELICULAS
        # ----------------------------------------------------

        self.mostrar_peliculas()

        # ----------------------------------------------------
        # SELECCIONAR PELICULA
        # ----------------------------------------------------

        while True:

            try:

                id_pelicula = int(
                    input("\nIngrese el ID de la película: ")
                )

                pelicula = self.vector_peliculas.buscar_por_id(
                    id_pelicula
                )

                if pelicula is None:

                    print("No existe una película con ese ID.")
                    continue

                break

            except ValueError:

                print("Ingrese un ID válido.")

        # ----------------------------------------------------
        # MOSTRAR ASIENTOS
        # ----------------------------------------------------

        self.matriz_asientos.mostrar()

        # ----------------------------------------------------
        # SELECCIONAR ASIENTO
        # ----------------------------------------------------

        while True:

            try:

                fila = int(
                    input("\nIngrese la fila del asiento: ")
                )

                columna = int(
                    input("Ingrese la columna del asiento: ")
                )

                asiento = self.matriz_asientos.obtener_asiento(
                    fila,
                    columna
                )

                if asiento is None:

                    print("El asiento seleccionado no existe.")
                    continue

                if not asiento.esta_disponible():

                    print("Ese asiento ya está ocupado.")
                    continue

                break

            except ValueError:

                print("Ingrese números válidos.")

        # ----------------------------------------------------
        # DATOS DE LA PERSONA
        # ----------------------------------------------------

        print("\n========== DATOS DEL CLIENTE ==========")

        nombre = input("Nombre completo: ").strip()

        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Nombre completo: ").strip()

        documento = input("Documento: ").strip()

        while documento == "":
            print("El documento no puede estar vacío.")
            documento = input("Documento: ").strip()

        while True:

            try:

                edad = int(
                    input("Edad: ")
                )

                if edad <= 0:
                    print("La edad debe ser mayor que 0.")
                    continue

                break

            except ValueError:

                print("Ingrese una edad válida.")

        # ----------------------------------------------------
        # CREAR PERSONA
        # ----------------------------------------------------

        persona = Persona(
            nombre,
            documento,
            edad
        )

        # ----------------------------------------------------
        # CREAR RESERVA
        # ----------------------------------------------------

        reserva = Reserva(
            persona,
            pelicula,
            asiento
        )

        # ----------------------------------------------------
        # OCUPAR ASIENTO
        # ----------------------------------------------------

        asiento.ocupar()

        # ----------------------------------------------------
        # GUARDAR RESERVA
        # ----------------------------------------------------

        self.lista_reservas.agregar(reserva)

        print("\n========================================")
        print("RESERVA REALIZADA CORRECTAMENTE")
        print("========================================")

        reserva.mostrar_reserva()


    # ========================================================
    # FUNCIONES DE SEBASTIAN
    # ========================================================

    def buscar_pelicula(self):
        pass

    def mostrar_reservas(self):
        pass

    def cancelar_reserva(self):
        pass


    # ========================================================
    # FUNCIONES DE NICOL
    # ========================================================
    # ========================================================
    # FUNCIONES DE NICOL
    # ========================================================

    def actualizar_pelicula(self):

        print("\n========== ACTUALIZAR PELÍCULA ==========")

        if len(self.vector_peliculas.obtener_todas()) == 0:
            print("No hay películas registradas.")
            return

        while True:

            try:
                id_pelicula = int(input("ID de la película a actualizar: "))
                break

            except ValueError:
                print("Ingrese un ID válido.")

        pelicula = self.vector_peliculas.buscar_por_id(id_pelicula)

        if pelicula is None:
            print("No existe una película con ese ID.")
            return

        print("\nPelícula encontrada:\n")
        pelicula.mostrar_informacion()

        print("\n(Deja vacío y presiona Enter para conservar el valor actual)")

        nuevo_titulo = input("Nuevo título: ").strip()
        nuevo_genero = input("Nuevo género: ").strip()

        while True:

            nueva_duracion = input("Nueva duración (minutos): ").strip()

            if nueva_duracion == "" or (nueva_duracion.isdigit() and int(nueva_duracion) > 0):
                break

            print("Entrada inválida: escribe un número mayor a 0 o deja vacío.")

        # La actualización se hace directamente sobre el objeto Pelicula
        if nuevo_titulo != "":
            pelicula.titulo = nuevo_titulo

        if nuevo_genero != "":
            pelicula.genero = nuevo_genero

        if nueva_duracion != "":
            pelicula.duracion = int(nueva_duracion)

        print("\nPelícula actualizada correctamente:\n")
        pelicula.mostrar_informacion()


    def eliminar_pelicula(self):

        print("\n========== ELIMINAR PELÍCULA ==========")

        if len(self.vector_peliculas.obtener_todas()) == 0:
            print("No hay películas registradas.")
            return

        self.mostrar_peliculas()

        while True:

            try:
                id_pelicula = int(input("\nID de la película a eliminar: "))
                break

            except ValueError:
                print("Ingrese un ID válido.")

        pelicula = self.vector_peliculas.buscar_por_id(id_pelicula)

        if pelicula is None:
            print("No existe una película con ese ID.")
            return

        # No se elimina si tiene reservas activas
        actual = self.lista_reservas.cabeza

        while actual is not None:

            if actual.dato.pelicula is pelicula:
                print("No se puede eliminar: la película tiene reservas activas.")
                return

            actual = actual.siguiente

        confirmar = input(f"¿Eliminar '{pelicula.titulo}'? (s/n): ").strip().lower()

        if confirmar == "s":
            self.vector_peliculas.eliminar_por_id(id_pelicula)
            print("Película eliminada correctamente.")

        else:
            print("Operación cancelada.")


    def mostrar_historial(self):

        print("\n========== HISTORIAL DE RESERVAS CANCELADAS ==========")

        if self.historial.esta_vacia():
            print("No hay reservas canceladas.")
            return

        print("\n--- Del inicio al final ---")
        self.historial.mostrar_inicio_fin()

        print("\n--- Del final al inicio ---")
        self.historial.mostrar_fin_inicio()
  
