import Participante
class Arbitro(Participante):
    def __init__(self, nombre, nacionalidad, categoria):
        super().__init__(nombre, nacionalidad)
        self.categoria = categoria
    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, value):
        if not isinstance(value, str):
            raise ValueError("La categoría debe ser una cadena de texto.")
        self._categoria = value
    def realizar_actividad(self):
        return f"El árbitro {self.nombre} está arbitrando en la categoría de {self.categoria}."