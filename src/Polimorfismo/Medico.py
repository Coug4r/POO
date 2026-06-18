from Participante import Participante
class Medico(Participante):
    def __init__(self, nombre, nacionalidad, especialidad):
        super().__init__(nombre, nacionalidad)
        self.especialidad = especialidad

    def realizar_actividad(self):
        return f"{self.nombre} está atendiendo a los jugadores con su especialidad en {self.especialidad}."