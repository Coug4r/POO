import Jugador
import Entrenador
import Arbritro

def main():
    participantes = []

    jugador1 = Jugador("Lionel Messi", "Argentina", "Delantero")
    entrenador1 = Entrenador("Diego Simeone", "Argentina", "Defensiva")
    arbitro1 = Arbritro("Pierluigi Collina", "Italia", "Árbitro Principal")

    print(jugador1.realizar_actividad())
    print(entrenador1.realizar_actividad())
    print(arbitro1.realizar_actividad())

if __name__ == "__main__":
    main()