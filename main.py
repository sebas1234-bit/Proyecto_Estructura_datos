# ============================================================
# PROYECTO CINE SANTA FE
# Estructuras de Datos - Python (versión terminal)
# Punto de entrada: solo el menú y el bucle principal
# ============================================================

from cine import Cine


def main():

    cine = Cine()

    while True:

        print("\n")
        print("========================================")
        print("          CINE SANTA FE")
        print("========================================")
        print("1. Agregar película")
        print("2. Mostrar películas")
        print("3. Buscar película")
        print("4. Actualizar película")
        print("5. Eliminar película")
        print("6. Reservar asiento")
        print("7. Ver reservas")
        print("8. Cancelar reserva")
        print("9. Ver historial")
        print("10. Salir")
        print("========================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            cine.agregar_pelicula()

        elif opcion == "2":
            cine.mostrar_peliculas()

        elif opcion == "3":
            cine.buscar_pelicula()

        elif opcion == "4":
            cine.actualizar_pelicula()

        elif opcion == "5":
            cine.eliminar_pelicula()

        elif opcion == "6":
            cine.reservar()

        elif opcion == "7":
            cine.mostrar_reservas()

        elif opcion == "8":
            cine.cancelar_reserva()

        elif opcion == "9":
            cine.mostrar_historial()

        elif opcion == "10":
            print("\nGracias por utilizar Cine Santa Fe.")
            break

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    main()