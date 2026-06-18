class Participante:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = value
    @property
    def nacionalidad(self):
        return self._nacionalidad
    @nacionalidad.setter
    def nacionalidad(self, value):
        if not isinstance(value, str):
            raise ValueError("La nacionalidad debe ser una cadena de texto.")
        self._nacionalidad = value
    def realizar_actividad(self):
        return f"El participante {self.nombre} está realizando una actividad."