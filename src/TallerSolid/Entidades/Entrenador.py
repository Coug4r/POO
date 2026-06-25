from Entidades.Participante import Participante
class Entrenador(Participante):
    def __init__(self, id_participante, nombre, nacionalidad, experiencia):
        super().__init__(id_participante, nombre, nacionalidad)
        self.experiencia = experiencia

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, value):
        self._experiencia = value
    
    def mostrar_informacion(self):
        return (super().mostrar_informacion() +
                f", Experiencia: {self.experiencia} años")