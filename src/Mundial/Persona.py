class Persona:
    def __init__(self, nombre, edad, pais):
        self.__nombre = nombre
        self.__edad = edad
        self.__pais = pais

    def get_nombre(self):
        return self.__nombre

    def mostrar_info(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("País:", self.__pais)