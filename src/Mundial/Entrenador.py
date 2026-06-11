from Persona import Persona

# Clase Entrenador que hereda de Persona
class Entrenador(Persona):

    def __init__(self, nombre, edad, pais, experiencia):
        super().__init__(nombre, edad, pais)
        self.__experiencia = experiencia

    @property
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter
    def experiencia(self, valor):
        if valor >= 0:
            self.__experiencia = valor

    def mostrar_info(self):
        print("\n--- Entrenador ---")
        super().mostrar_info()
<<<<<<< HEAD:src/Entrenador
        print("Experiencia:", self.experiencia, "años")
=======
        print("Experiencia:", self.__experiencia)
>>>>>>> ab5f442b30ec4c912ca057559aefab2c3b4663c6:src/Mundial/Entrenador.py
