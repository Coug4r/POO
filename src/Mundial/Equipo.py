# Clase Equipo
class Equipo:

    def __init__(self, nombre, pais, entrenador):
        self._nombre = nombre
        self._pais = pais
        self._entrenador = entrenador
        self.__jugadores = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def pais(self):
        return self._pais

    @property
    def entrenador(self):
        return self._entrenador

    @property
    def jugadores(self):
        return self.__jugadores

    def agregar_jugador(self, jugador):
        self.__jugadores.append(jugador)

    def mostrar_equipo(self):
        print("\n======================")
        print("Equipo:", self.nombre)
        print("País:", self.pais)

        print("\nEntrenador:")
        self.entrenador.mostrar_info()

        print("\nJugadores:")
<<<<<<< HEAD:src/Equipo
        for jugador in self.jugadores:
            jugador.mostrar_info()
=======
        for jugador in self.__jugadores:
            jugador.mostrar_info()
>>>>>>> ab5f442b30ec4c912ca057559aefab2c3b4663c6:src/Mundial/Equipo.py
