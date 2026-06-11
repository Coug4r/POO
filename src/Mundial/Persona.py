# Clase base Persona
class Persona:
<<<<<<< HEAD:src/Persona

    def __init__(self, nombre, edad, pais):
        self._nombre = nombre
        self._edad = edad
        self._pais = pais

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def pais(self):
        return self._pais

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("País:", self.pais)
=======
    def __init__(self, nombre, edad, pais):
        # Atributos privados
        self.__nombre = nombre
        self.__edad = edad
        self.__pais = pais

    def get_nombre(self):
        # Devuelve el nombre de la persona
        return self.__nombre

    def mostrar_info(self):
        # Muestra la información básica de la persona
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("País:", self.__pais)
>>>>>>> ab5f442b30ec4c912ca057559aefab2c3b4663c6:src/Mundial/Persona.py
