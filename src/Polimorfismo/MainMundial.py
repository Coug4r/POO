from Jugador import Jugador
from Entrenador import Entrenador
from Arbritro import Arbitro

def main():
    participantes = [(Jugador("Lionel Messi", "Argentina", "Delantero")),(Entrenador("Diego Simeone", "Argentina", "Defensiva")),(Arbitro("Pierluigi Collina", "Italia", "Árbitro Principal"))]
    for participante in participantes:
        print(participante.realizar_actividad())

if __name__ == "__main__":
    main()