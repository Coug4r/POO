from Entidades.Participante import Participante
from Interfaces.Notificacion import Notificacion
from Interfaces.Reporte import Reporte
from Interfaces.Persistencia import Persistencia
datos = "./datos.pkl"
participantes = []
class GestorMundial:
    def __init__(self, servicio_notificacion: Notificacion, 
                 generador_reporte: Reporte, 
                 repositorio: Persistencia):
        self.servicio_notificacion = servicio_notificacion
        self.generador_reporte = generador_reporte
        self.repositorio = repositorio
        self._ultimaId = 0

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
