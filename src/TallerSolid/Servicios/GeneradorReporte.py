from Interfaces.Reporte import Reporte

class GeneradorReporte(Reporte):
    def generar(self, participantes: list) -> str:
        # Implementación de la generación de reporte 
        reporte = "=== Reporte de Participantes ===\n"
        for p in participantes:
            # Mostrar atributos comunes
            reporte += f"ID: {p.id_participante}, Nombre: {p.nombre}, País: {p.nacionalidad}"

            # Si es Jugador, añadir atributos específicos
            if hasattr(p, "posicion") and hasattr(p, "numero_camiseta"):
                reporte += f", Posición: {p.posicion}, Camiseta: {p.numero_camiseta}"
            # Si es Árbitro, añadir atributos específicos
            elif hasattr(p, "categoria"):
                reporte += f", Categoría: {p.categoria}"    
            # Si es Entrenador, añadir atributos específicos
            elif hasattr(p, "experiencia"):
                reporte += f", Experiencia: {p.experiencia} años"
            reporte += "\n"
        return reporte

    def mostrar(self, reporte: str) -> None:
        # Implementación de la visualización del reporte
        print(reporte)
