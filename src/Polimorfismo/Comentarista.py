from Participante import Participante
class Comentarista(Participante):
    def __init__(self, nombre, nacionalidad, especialidad):
        super().__init__(nombre, nacionalidad)
        self.especialidad = especialidad

    def realizar_actividad(self):
        return f"{self.nombre} está comentando el partido con su especialidad en {self.especialidad}."