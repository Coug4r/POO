from Servicios.ServicioNotificacion import ServicioNotificacion
from Servicios.GeneradorReporte import GeneradorReporte
from Servicios.Repositorio import Repositorio
from Entidades.Participante import Participante
datos = "./datos.pkl"
participantes = []
class GestorMundial:
    def __init__(self):
        self.servicio_notificacion = ServicioNotificacion()
        self.generador_reporte = GeneradorReporte()
        self.repositorio = Repositorio(datos)
        self._ultimaId = 0   # atributo privado para manejar el ID

    def guardar_participantes(self, participante: Participante) -> None:
        participantes = self.repositorio.cargar()
        participantes.append(participante)
        self.repositorio.guardar(participantes)
        self.servicio_notificacion.enviar("Participante guardado correctamente.")

    def generar_reporte(self) -> None:
        participantes = self.repositorio.cargar()
        reporte = self.generador_reporte.generar(participantes)
        self.generador_reporte.mostrar(reporte)
        self.servicio_notificacion.enviar("Reporte generado correctamente.")

    def persistir_informacion(self, participantes: list) -> None:
        self.repositorio.guardar(participantes)
        self.servicio_notificacion.enviar("Información de participantes respaldada correctamente.")
    def mostrar_informacion(self) -> None:
        participantes = self.repositorio.cargar()
        for p in participantes:
            print(p.mostrar_informacion())   

    # Getter
    @property
    def ultimaId(self):
        return self._ultimaId

    # Setter
    @ultimaId.setter
    def ultimaId(self, nuevaId):
        if nuevaId > self._ultimaId:
            self._ultimaId = nuevaId
        else:
            raise ValueError("El ID ya existe o no es válido")
