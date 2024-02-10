# Alumno : Sebastian Sanchez Bentolila 

# Módulo Expresiones Regulares - Aplicación {gestor de contactos}

# Librerías
from re import match
from tkinter import messagebox

# Expresiones regulares para verificar mail, nombre y telefono
telefono_pattern = r'^\d{10}$' # Admite 10 números
correo_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' # Formato mail estandar
nombre_pattern = r'^[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+$' # Caracteres alfanuméricos con posibilidad de espacios en blanco

# Funciones
def validar_expresiones(telefono, nombre, mail):
    # Módulo que permite validar las expresiones dadas por el usuario y devuelve True o False dependiendo el caso
    global telefono_pattern, correo_pattern, nombre_pattern
    telefono_validado=False
    nombreo_validado=False
    mail_validado=False
    
    # Validar el teléfono
    if telefono and not match(telefono_pattern, telefono):
        messagebox.showerror("Error", "El nuevo teléfono no es válido")
        return
    else:
        telefono_validado=True
    
    # Validar el nombre 
    if nombre and not match(nombre_pattern, nombre):
        messagebox.showerror("Error", "El nombre solo admite caracteres alfanúmericos")
        return
    else:
        nombreo_validado=True
        
    # Validar el correo electrónico 
    if mail and not match(correo_pattern, mail):
        messagebox.showerror("Error", "El nuevo correo electrónico no es válido")
        return
    else:
        mail_validado=True
    
    return telefono_validado, nombreo_validado, mail_validado