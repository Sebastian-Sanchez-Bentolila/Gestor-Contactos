# Alumno : Sebastian Sanchez Bentolila

# Servidor - Aplicación {gestor de contactos}

# Librerías 
import socket
import threading
import sys

# Clases
class Servidor:
    # Servidor con socket
    
    # Atributos
    def __init__(self, host, port, observador):
        self.host = host
        self.port = port
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.clientes_conectados = []
        self.observador = observador

    # Métodos 
    def iniciar(self):
        try:
            self.socket_servidor.listen()
            self.observador.actualizar(f"Servidor iniciado en {self.host}:{self.port}")

            while True:
                cliente, direccion = self.socket_servidor.accept()
                self.observador.actualizar(f"Cliente conectado desde {direccion}")
                self.clientes_conectados.append(cliente)

                # Iniciar un hilo para manejar la comunicación con el cliente
                hilo_cliente = threading.Thread(target=self.atender_cliente, args=(cliente,))
                hilo_cliente.start()
        except Exception as e:
            print(f"Error al iniciar el servidor: {e}")
            sys.exit(1)

    def atender_cliente(self, cliente):
        try:
            while True:
                datos = cliente.recv(1024)
                if not datos:
                    break
                mensaje = datos.decode('utf-8')
                self.observador.actualizar(f"Mensaje recibido: {mensaje}")
        except Exception as e:
            self.observador.actualizar(f"Error al atender cliente: {e}")
        finally:
            cliente.close()
            self.clientes_conectados.remove(cliente)

    def detener(self):
        try:
            self.socket_servidor.close()
            self.observador.actualizar("Servidor detenido")
        except Exception as e:
            print(f"Error al detener el servidor: {e}")
            sys.exit(1)      