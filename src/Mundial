class Mundial:
    def __init__(self, nombre, sede, anio):
        self.__nombre = nombre
        self.__sede = sede
        self.__anio = anio
        self.__equipos = []
        self.__partidos = []

    def agregar_equipo(self, equipo):
        self.__equipos.append(equipo)

    def agregar_partido(self, partido):
        self.__partidos.append(partido)

    def buscar_equipo(self, nombre):
        for equipo in self.__equipos:
            if equipo.get_nombre().lower() == nombre.lower():
                return equipo
        return None

    def mostrar_mundial(self):
        print("\n========== MUNDIAL ==========")
        print("Nombre:", self.__nombre)
        print("Sede:", self.__sede)
        print("Año:", self.__anio)

    def mostrar_equipos(self):
        for equipo in self.__equipos:
            equipo.mostrar_equipo()

    def mostrar_partidos(self):
        if len(self.__partidos) == 0:
            print("No hay partidos registrados.")
        else:
            for partido in self.__partidos:
                partido.mostrar_partido()