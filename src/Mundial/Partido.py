# Clase Partido
class Partido:
    def __init__(self, equipo1, equipo2, fecha, estadio):
        self.__equipo1 = equipo1
        self.__equipo2 = equipo2
        self.__fecha = fecha
        self.__estadio = estadio
        self.__goles1 = 0
        self.__goles2 = 0

    def registrar_resultado(self, goles1, goles2):
        self.__goles1 = goles1
        self.__goles2 = goles2

    def mostrar_partido(self):
        print("\nPartido")
        print(self.__equipo1.get_nombre(), "vs", self.__equipo2.get_nombre())
        print("Resultado:", self.__goles1, "-", self.__goles2)
