from Persona import Persona

class Entrenador(Persona):
    def __init__(self, nombre, edad, pais, experiencia):
        super().__init__(nombre, edad, pais)
        self.__experiencia = experiencia

    def mostrar_info(self):
        print("\n--- Entrenador ---")
        super().mostrar_info()
        print("Experiencia:", self.__experiencia)