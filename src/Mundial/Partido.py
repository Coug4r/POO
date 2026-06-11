# Clase Partido
class Partido:

    def __init__(self, equipo1, equipo2, fecha, estadio):
        self._equipo1 = equipo1
        self._equipo2 = equipo2
        self._fecha = fecha
        self._estadio = estadio

        self.__goles1 = 0
        self.__goles2 = 0

    @property
    def equipo1(self):
        return self._equipo1

    @property
    def equipo2(self):
        return self._equipo2

    @property
    def fecha(self):
        return self._fecha

    @property
    def estadio(self):
        return self._estadio

    @property
    def goles1(self):
        return self.__goles1

    @property
    def goles2(self):
        return self.__goles2

    def registrar_resultado(self, goles1, goles2):
        self.__goles1 = goles1
        self.__goles2 = goles2

    def mostrar_partido(self):
<<<<<<< HEAD:src/Partido
        print("\n========== PARTIDO ==========")
        print("Fecha:", self.fecha)
        print("Estadio:", self.estadio)
        print(self.equipo1.nombre, "vs", self.equipo2.nombre)
        print("Resultado:", self.goles1, "-", self.goles2)
=======
        print("\nPartido")
        print(self.__equipo1.get_nombre(), "vs", self.__equipo2.get_nombre())
        print("Resultado:", self.__goles1, "-", self.__goles2)
>>>>>>> ab5f442b30ec4c912ca057559aefab2c3b4663c6:src/Mundial/Partido.py
