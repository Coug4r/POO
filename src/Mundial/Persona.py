# Clase base Persona
class Persona:
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
