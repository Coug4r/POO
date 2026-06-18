import Participante
class Entrenador(Participante):
    def __init__(self, nombre, nacionalidad, estrategia):
        super().__init__(nombre, nacionalidad)
        self.estrategia = estrategia
    @property
    def estrategia(self):
        return self._estrategia
    @estrategia.setter
    def estrategia(self, value):
        if not isinstance(value, str):
            raise ValueError("La estrategia debe ser una cadena de texto.")
        self._estrategia = value
    def realizar_actividad(self):
        return f"El entrenador {self.nombre} está implementando la estrategia de {self.estrategia}."