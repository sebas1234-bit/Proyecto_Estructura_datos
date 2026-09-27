# ============================================================
# CLASE PERSONA
# ============================================================

class Persona:

    def __init__(self, nombre, documento, edad):
        self.nombre = nombre
        self.documento = documento
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Edad: {self.edad}")