from Servicios.GestorMundial import GestorMundial
from Entidades.Jugador import Jugador
from Entidades.Arbitro import Arbitro
from Entidades.Entrenador import Entrenador
from Servicios.ServicioNotificacion import ServicioNotificacion
from Servicios.GeneradorReporte import GeneradorReporte
from Servicios.Repositorio import Repositorio
def main():
    gestor = GestorMundial(
        ServicioNotificacion(),
        GeneradorReporte(),
        Repositorio("./datos.pkl"))
    participante = None
    #Menu para usuario para agregar participantes a partir de entidades y generar reporte
    while True:
        print("1. Agregar participante")
        print("2. Generar reporte")
        print("3. Mostrar información")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("1.Jugador")
            print("2.Arbitro")
            print("3.Entrenador")
            tipo = input("Opcion: ")
            match tipo:
                case "1":
                    nombre = input("Ingrese el nombre del participante: ")
                    pais = input("Ingrese el país del participante: ")
                    posision = input("Ingrese la posicion en la que juega: ")
                    numero_camiseta = input("Ingrese el numero de la camiseta: ")
                    gestor.ultimaId = gestor.ultimaId + 1
                    participante = Jugador(gestor.ultimaId, nombre, pais, posision, numero_camiseta)
                    gestor.guardar_participantes(participante)
                case "2":   # Árbitro
                    nombre = input("Ingrese el nombre del árbitro: ")
                    pais = input("Ingrese el país del árbitro: ")
                    categoria = input("Ingrese la categoría del árbitro: ")

                    gestor.ultimaId = gestor.ultimaId + 1
                    participante = Arbitro(gestor.ultimaId, nombre, pais, categoria)
                    gestor.guardar_participantes(participante)

                case "3":   # Entrenador
                    nombre = input("Ingrese el nombre del entrenador: ")
                    pais = input("Ingrese el país del entrenador: ")
                    experiencia = input("Ingrese los años de experiencia: ")

                    gestor.ultimaId = gestor.ultimaId + 1
                    participante = Entrenador(gestor.ultimaId, nombre, pais, experiencia)
                    gestor.guardar_participantes(participante)

                case _:     # Opción inválida
                    print("Tipo de participante inválido.")
                

        elif opcion == "2":
            gestor.generar_reporte()
        elif opcion == "3":
            gestor.mostrar_informacion()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()