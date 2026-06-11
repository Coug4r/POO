# Clase Equipo
class Equipo:
    def __init__(self, nombre, pais, entrenador):
        self.__nombre = nombre
        self.__pais = pais
        self.__entrenador = entrenador
        self.__jugadores = []

    def get_nombre(self):
        return self.__nombre

    def agregar_jugador(self, jugador):
        self.__jugadores.append(jugador)

    def mostrar_equipo(self):
        print("\nEquipo:", self.__nombre)
        print("País:", self.__pais)

        print("\nEntrenador:")
        self.__entrenador.mostrar_info()

        print("\nJugadores:")
        for jugador in self.__jugadores:
            jugador.mostrar_info()
