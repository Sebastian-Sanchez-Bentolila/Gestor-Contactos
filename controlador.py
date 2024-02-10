# Alumno : Sebastian Sanchez Bentolila

# Controlador - Aplicación {gestor de contactos}

# Librerías
from tkinter import Tk
from vista import ventana_grafica
from red.cliente import Cliente
from red.servidor import Servidor
from log.observador import ObservadorRegistro
import threading

# Bucle principal
def iniciar_aplicacion():
    # Iniciar Servidor 
    observador_registro = ObservadorRegistro('log\\registro_log.txt')
    servidor = Servidor('192.168.56.1', 456, observador_registro)
    hilo_servidor = threading.Thread(target=servidor.iniciar)
    hilo_servidor.start()
    #servidor.iniciar()
    
    # Cliente 
    cliente = Cliente('192.168.56.1', 456)
    mensaje_inicio = "Cliente conectado"
    cliente.enviar_mensaje(mensaje_inicio)
    
    # Ventana Gráfica
    root = Tk()       
    app = ventana_grafica(root)
    
    # Cerrando Conexión
    mensaje_cierre = "Cliente desconectado"
    cliente.enviar_mensaje(mensaje_cierre)
    cliente.cerrar_conexion()
    
    # Cerrando Servidor
    servidor.detener()
    hilo_servidor.join()