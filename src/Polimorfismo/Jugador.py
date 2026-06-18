import Participante
class jugdor(Participante):
    def __init__(self, nombre, nacionalidad, posicion):
        super().__init__(nombre, nacionalidad)
        self.posicion = posicion
    @property
    def posicion(self):
        return self._posicion
    @posicion.setter
    def posicion(self, value):
        if not isinstance(value, str):
            raise ValueError("La posición debe ser una cadena de texto.")
        self._posicion = value
    def realizar_actividad(self):
        return f"El jugador {self.nombre} está jugando en la posición de {self.posicion}."