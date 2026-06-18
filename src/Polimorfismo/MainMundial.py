from Jugador import Jugador
from Entrenador import Entrenador
from Arbritro import Arbitro
from Comentarista import Comentarista
from Medico import Medico
def main():
    participantes = [(Jugador("Lionel Messi", "Argentina", "Delantero")),
                     (Entrenador("Diego Simeone","Argentina", "Defensiva")),
                     (Arbitro("Pierluigi Collina", "Italia", "Árbitro Principal")),
                     (Comentarista("Andrés Cantor", "Argentina", "Narración")),
                     (Medico("Dr. Juan Pérez", "Argentina", "Medicina Deportiva"))]
    for participante in participantes:
        print(participante.realizar_actividad())

if __name__ == "__main__":
    main()