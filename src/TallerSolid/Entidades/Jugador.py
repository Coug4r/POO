from Entidades.Participante import Participante
class Jugador(Participante):
    def __init__(self, id_participante, nombre, nacionalidad, posicion, numero_camiseta):
        super().__init__(id_participante, nombre, nacionalidad)
        self.posicion = posicion
        self.numero_camiseta = numero_camiseta
    @property
    def posicion(self):
        return self._posicion
    @posicion.setter
    def posicion(self, value):
        self._posicion = value
    @property
    def numero_camiseta(self):
        return self._numero_camiseta
    @numero_camiseta.setter
    def numero_camiseta(self, value):
        self._numero_camiseta = value
        
    def mostrar_informacion(self):
        return (super().mostrar_informacion() +
                f", Posición: {self.posicion}, Camiseta: {self.numero_camiseta}")
    