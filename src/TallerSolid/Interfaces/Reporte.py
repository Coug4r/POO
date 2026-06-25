from abc import ABC, abstractmethod
class Reporte(ABC):
    @abstractmethod
    def generar(self, datos: dict) -> str:
        pass