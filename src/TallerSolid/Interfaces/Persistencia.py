from abc import ABC, abstractmethod
class Persistencia(ABC):
    @abstractmethod
    def guardar(self, datos: dict) -> None:
        pass

    @abstractmethod
    def cargar(self) -> dict:
        pass