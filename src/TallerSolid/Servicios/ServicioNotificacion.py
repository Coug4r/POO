from Interfaces.Notificacion import Notificacion
class ServicioNotificacion(Notificacion):
    def enviar(self, mensaje: str) -> None:
        # Implementación del envío de notificación
        print(f"Enviando notificación: {mensaje}")