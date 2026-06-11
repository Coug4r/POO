from Mundial import Mundial
from Equipo import Equipo
from Jugador import Jugador
from Entrenador import Entrenador
from Partido import Partido
# Crear el Mundial
mundial = Mundial("Mundial de Fútbol", "Estados Unidos, México y Canadá", 2026)


# Función para crear equipos con jugadores
def crear_equipo(nombre_equipo, pais, entrenador_nombre, entrenador_edad, experiencia, jugadores):
    entrenador = Entrenador(entrenador_nombre, entrenador_edad, pais, experiencia)
    equipo = Equipo(nombre_equipo, pais, entrenador)

    for jugador in jugadores:
        equipo.agregar_jugador(
            Jugador(jugador[0], jugador[1], pais, jugador[2], jugador[3], jugador[4])
        )

    mundial.agregar_equipo(equipo)


# Equipos iniciales con 3 jugadores

crear_equipo("Ecuador", "Ecuador", "Sebastián Beccacece", 43, 15, [
    ("Moisés Caicedo", 24, "Mediocampista", 23, 2),
    ("Piero Hincapié", 24, "Defensa", 3, 1),
    ("Enner Valencia", 36, "Delantero", 13, 6)
])

crear_equipo("Argentina", "Argentina", "Lionel Scaloni", 47, 10, [
    ("Lionel Messi", 38, "Delantero", 10, 13),
    ("Julián Álvarez", 26, "Delantero", 9, 5),
    ("Emiliano Martínez", 33, "Arquero", 23, 0)
])

crear_equipo("Brasil", "Brasil", "Dorival Júnior", 63, 25, [
    ("Vinícius Jr.", 25, "Delantero", 7, 5),
    ("Rodrygo", 25, "Delantero", 11, 4),
    ("Alisson Becker", 33, "Arquero", 1, 0)
])

crear_equipo("Francia", "Francia", "Didier Deschamps", 57, 20, [
    ("Kylian Mbappé", 27, "Delantero", 10, 12),
    ("Antoine Griezmann", 35, "Mediocampista", 7, 8),
    ("Mike Maignan", 30, "Arquero", 16, 0)
])


# Partidos iniciales

p1 = Partido(mundial.buscar_equipo("Ecuador"), mundial.buscar_equipo("Argentina"), "15/06/2026", "Estadio Azteca")
p1.registrar_resultado(1, 2)
mundial.agregar_partido(p1)

p2 = Partido(mundial.buscar_equipo("Brasil"), mundial.buscar_equipo("Francia"), "18/06/2026", "MetLife Stadium")
p2.registrar_resultado(2, 2)
mundial.agregar_partido(p2)


# Menú principal

while True:
    print("\n===== SISTEMA DEL MUNDIAL DE FÚTBOL =====")
    print("1. Mostrar información del Mundial")
    print("2. Mostrar todos los equipos")
    print("3. Mostrar partidos")
    print("4. Registrar nuevo equipo")
    print("5. Registrar jugador en un equipo")
    print("6. Registrar nuevo partido")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mundial.mostrar_mundial()

    elif opcion == "2":
        mundial.mostrar_equipos()

    elif opcion == "3":
        mundial.mostrar_partidos()

    elif opcion == "4":
        nombre_equipo = input("Nombre del equipo: ")
        pais = input("País: ")

        nombre_entrenador = input("Nombre del entrenador: ")
        edad_entrenador = int(input("Edad del entrenador: "))
        experiencia = int(input("Años de experiencia: "))

        entrenador = Entrenador(nombre_entrenador, edad_entrenador, pais, experiencia)
        equipo = Equipo(nombre_equipo, pais, entrenador)

        mundial.agregar_equipo(equipo)
        print("Equipo registrado correctamente.")

    elif opcion == "5":
        nombre_equipo = input("Nombre del equipo: ")
        equipo = mundial.buscar_equipo(nombre_equipo)

        if equipo is None:
            print("Equipo no encontrado.")
        else:
            nombre = input("Nombre del jugador: ")
            edad = int(input("Edad: "))
            pais = input("País: ")
            posicion = input("Posición: ")
            numero = int(input("Número de camiseta: "))
            goles = int(input("Goles: "))

            jugador = Jugador(nombre, edad, pais, posicion, numero, goles)
            equipo.agregar_jugador(jugador)

            print("Jugador agregado correctamente.")

    elif opcion == "6":
        nombre1 = input("Nombre del primer equipo: ")
        nombre2 = input("Nombre del segundo equipo: ")

        equipo1 = mundial.buscar_equipo(nombre1)
        equipo2 = mundial.buscar_equipo(nombre2)

        if equipo1 is None or equipo2 is None:
            print("Uno de los equipos no existe.")
        else:
            fecha = input("Fecha del partido: ")
            estadio = input("Estadio: ")
            goles1 = int(input("Goles del primer equipo: "))
            goles2 = int(input("Goles del segundo equipo: "))

            partido = Partido(equipo1, equipo2, fecha, estadio)
            partido.registrar_resultado(goles1, goles2)

            mundial.agregar_partido(partido)
            print("Partido registrado correctamente.")

    elif opcion == "7":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción incorrecta.")