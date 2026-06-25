from Entidades.Participante import Participante
class Arbitro(Participante):
    def __init__(self, id_participante, nombre, nacionalidad, categoria):
        super().__init__(id_participante, nombre, nacionalidad)
        self.categoria = categoria

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value

    def mostrar_informacion(self):
        return (super().mostrar_informacion() +
                f", Categoría: {self.categoria}")