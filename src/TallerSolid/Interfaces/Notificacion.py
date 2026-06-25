from abc import ABC, abstractmethod
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass