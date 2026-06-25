import pickle
import os
from Interfaces.Persistencia import Persistencia

class Repositorio(Persistencia):
    def __init__(self, archivo: str):
        self.archivo = archivo
        carpeta = os.path.dirname(archivo)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)

    def guardar(self, datos) -> None:   # puede ser dict, lista, objeto...
        with open(self.archivo, 'wb') as f:
            pickle.dump(datos, f)

    def cargar(self):
        try:
            with open(self.archivo, 'rb') as f:
                datos = pickle.load(f)
            return datos
        except FileNotFoundError:
            return []   # si no existe, devuelve lista vacía
