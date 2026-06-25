class Participante:
    def __init__(self, id_participante, nombre, nacionalidad):
        self.id_participante = id_participante
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    @property
    def id_participante(self):
        return self._id_participante
    @id_participante.setter
    def id_participante(self, value):
        self._id_participante = value
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
    @property
    def nacionalidad(self):
        return self._nacionalidad
    @nacionalidad.setter
    def nacionalidad(self, value):
        self._nacionalidad = value
    
    def mostrar_informacion(self):
        return f"ID: {self.id_participante}, Nombre: {self.nombre}, País: {self.nacionalidad}"