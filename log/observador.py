# Alumno : Sebastian Sanchez Bentolila 

# Clase Observador - Aplicación {gestor de contactos}

# Librerías
from datetime import datetime

# Clases
class Observador:
    # Observador
    def actualizar(self, mensaje):
        raise NotImplementedError("Subclases de Observador")

class ObservadorRegistro(Observador):
    # Observador para registrar eventos registro_log.txt
    def __init__(self, archivo_registro):
        self.archivo_registro = archivo_registro

    def actualizar(self, mensaje):
        # Guardar el mensaje en el archivo de registro con la fecha y hora actual
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.archivo_registro, 'a') as file:
            file.write(f"{timestamp} - {mensaje}\n")
