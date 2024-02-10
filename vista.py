# Alumno : Sebastian Sanchez Bentolila 

# Vista - Aplicación {gestor de contactos}

# Librerías
from tkinter import Tk, messagebox, Scrollbar, Label, Entry, Button, Text, VERTICAL, END
from os import getcwd, remove
from modelo import BaseDatos
from modulos.expresiones import validar_expresiones
from log.observador import ObservadorRegistro
from red.servidor import Servidor

# Clases
class ventana_grafica():
    # Clase de la ventana gráfica 
    
    # Configuracion de la ventana principal
    def __init__(self, root):
        self.ventana = root
        self.db = BaseDatos()
        self.observador_registro = ObservadorRegistro('log\\registro_log.txt')
        self.db.agregar_observador(self.observador_registro)
        self.ventana.title("Gestor de Contactos")
        self.ventana.iconbitmap('{}\\archivos\\icon\\libro_contacto.ico'.format(getcwd()))
        self.ventana.configure(bg="blue", cursor='tcross')
        self.ventana.resizable(0, 0)
        self.Widgets()
        self.ventana.mainloop()
        
    # Métodos 
    def Widgets(self,):
        # Accesorios de la ventana gráfica
        # Sección - Agregar contacto
        Label(self.ventana, text="Teléfono:", bg="blue", fg="white").grid(row=1, column=0)
        self.telefono_entry = Entry(self.ventana, bg="lightblue")
        self.telefono_entry.grid(row=1, column=1)

        Label(self.ventana, text="Nombre:", bg="blue", fg="white").grid(row=2, column=0)
        self.nombre_entry = Entry(self.ventana, bg="lightblue")
        self.nombre_entry.grid(row=2, column=1)

        Label(self.ventana, text="Empresa:", bg="blue", fg="white").grid(row=3, column=0)
        self.empresa_entry = Entry(self.ventana, bg="lightblue")
        self.empresa_entry.grid(row=3, column=1)

        Label(self.ventana, text="Correo:", bg="blue", fg="white").grid(row=4, column=0)
        self.mail_entry = Entry(self.ventana,bg="lightblue")
        self.mail_entry.grid(row=4, column=1)

        Label(self.ventana, text="Relacion:", bg="blue", fg="white").grid(row=5, column=0)
        self.relacion_entry = Entry(self.ventana, bg="lightblue")
        self.relacion_entry.grid(row=5, column=1)

        self.agregar_btn = Button(self.ventana, text="Agregar Contacto", bg="gray", fg="black", command=self.agregar_contacto)
        self.agregar_btn.grid(row=6, column=0, columnspan=2)
        
        # Sección - Buscar Contacto
        Label(self.ventana, text="Buscar por nombre:", bg="blue", fg="white").grid(row=8, column=0)
        self.nombre_buscar_entry = Entry(self.ventana, bg="lightblue")
        self.nombre_buscar_entry.grid(row=8, column=1)

        self.buscar_btn = Button(self.ventana, text="Buscar Contacto", bg="gray", fg="black", command=self.seleccionar_contacto)
        self.buscar_btn.grid(row=9, column=0, columnspan=2)
        
        # Sección - Resultado de la busqueda de contacto
        self.resultado_text = Text(self.ventana, height=10, width=40, bg="lightblue", fg="black")
        self.resultado_text.grid(row=10, column=0, columnspan=2)
        
        # Sección - Borrar Contacto
        Label(self.ventana, text="Borrar por nombre:", bg="blue", fg="white").grid(row=5, column=4)
        self.nombre_borrar_entry = Entry(self.ventana, bg="lightblue")
        self.nombre_borrar_entry.grid(row=5, column=5)

        self.borrar_btn = Button(self.ventana, text="Borrar Contacto", bg="gray", fg="black", command=self.borrar_contacto)
        self.borrar_btn.grid(row=6, column=4, columnspan=2)
        
        # Seccion - Modificar Contacto
        Label(self.ventana, text="ID del contacto a modificar:", bg="blue", fg="white").grid(row=0, column=2)
        self.id_modificar_entry = Entry(self.ventana, bg="lightblue")
        self.id_modificar_entry.grid(row=0, column=3)

        Label(self.ventana, text="Nuevo teléfono:", bg="blue", fg="white").grid(row=1, column=2)
        self.nuevo_telefono_entry = Entry(self.ventana, bg="lightblue")
        self.nuevo_telefono_entry.grid(row=1, column=3)

        Label(self.ventana, text="Nuevo nombre:", bg="blue", fg="white").grid(row=2, column=2)
        self.nuevo_nombre_entry = Entry(self.ventana, bg="lightblue")
        self.nuevo_nombre_entry.grid(row=2, column=3)

        Label(self.ventana, text="Nueva empresa:", bg="blue", fg="white").grid(row=3, column=2)
        self.nueva_empresa_entry = Entry(self.ventana, bg="lightblue")
        self.nueva_empresa_entry.grid(row=3, column=3)

        Label(self.ventana, text="Nuevo correo:", bg="blue", fg="white").grid(row=4, column=2)
        self.nuevo_mail_entry = Entry(self.ventana, bg="lightblue")
        self.nuevo_mail_entry.grid(row=4, column=3)

        Label(self.ventana, text="Nueva relacion:", bg="blue", fg="white").grid(row=5, column=2)
        self.nuevo_relacion_entry = Entry(self.ventana, bg="lightblue")
        self.nuevo_relacion_entry.grid(row=5, column=3)

        self.modificar_btn = Button(self.ventana, text="Modificar Contacto", bg="gray", fg="black", command=self.modificar_contacto)
        self.modificar_btn.grid(row=6, column=2, columnspan=2)
        
        # Sección - Lista de Contactos
        self.lista_btn = Button(self.ventana, text="Ver contactos", bg="gray", fg="black", command=self.abrir_lista_contactos)
        self.lista_btn.grid(row=9, column=2, columnspan=2)

        self.lista_text = Text(self.ventana, height=10, width=40, bg="lightblue", fg="black")
        self.lista_text.grid(row=10, column=3, columnspan=3)
        self.agregar_scrollbar()
        
        # Agregando una columna vacia para generar una separación entre arriba y abajo
        self.espacio = Label(self.ventana, text="", bg="blue", fg="white").grid(row=7, column=0, columnspan=2)
        
    def agregar_scrollbar(self,):
        # Scrollbar para la Sección de lista de contactos
        self.scrollbar = Scrollbar(self.ventana, orient=VERTICAL ,command=self.lista_text.yview)
        self.scrollbar.grid(row=10, column=6, rowspan=3, sticky='ns')
        self.lista_text.config(yscrollcommand=self.scrollbar.set)
        
    def modificar_contacto(self,):
        # Comando para modificar algun contacto
        id_contacto = self.id_modificar_entry.get()
        nuevo_telefono = self.nuevo_telefono_entry.get()
        nuevo_nombre = self.nuevo_nombre_entry.get()
        nueva_empresa = self.nueva_empresa_entry.get()
        nuevo_mail = self.nuevo_mail_entry.get()
        nuevo_relacion = self.nuevo_relacion_entry.get()
        
        if id_contacto and (nuevo_telefono or nuevo_nombre or nueva_empresa or nuevo_mail or nuevo_relacion):
            expresiones_validas = validar_expresiones(nuevo_telefono, nuevo_nombre, nuevo_mail)
            if expresiones_validas:
                x, y, z = expresiones_validas # x,y,z son las validaciónes de esos campos (boleanos)
                if x and y and z:
                    try:
                        if self.db.verificar_existencia_contacto_por_id(id_contacto):
                            self.db.actualizar(int(id_contacto), int(nuevo_telefono), nuevo_nombre, nueva_empresa, nuevo_mail, nuevo_relacion)
                            messagebox.showinfo("Éxito", "Contacto modificado con éxito")
                        else:
                            messagebox.showerror("Error", f"No se encontró un contacto con el ID '{id_contacto}'")
                    except Exception as e:
                        messagebox.showerror("Error", f"Error al modificar el contacto: {str(e)}")
                else:
                    pass
        else:
            messagebox.showerror("Error", "ID del contacto y el telefono son campos obligatorios")
            
    def agregar_contacto(self,):
        # Comando para agregar un contacto a la db
        telefono = self.telefono_entry.get()
        nombre = self.nombre_entry.get()
        empresa = self.empresa_entry.get()
        mail = self.mail_entry.get()
        relacion = self.relacion_entry.get()
        
        if telefono and nombre:
            expresiones_validas = validar_expresiones(telefono, nombre, mail)
            if expresiones_validas:
                x, y, z = expresiones_validas # x,y,z son las validaciónes de esos campos (boleanos)
                if x and y and z:
                    try:
                        self.db.insertar(telefono, nombre, empresa, mail, relacion)
                        messagebox.showinfo("Éxito", "Contacto agregado con éxito")
                    except Exception as e:
                        messagebox.showerror("Error", f"Error al agregar el contacto: {str(e)}")
            else:
                pass
        else:
            messagebox.showerror("Error", "El nombre y el teléfono son campos obligatorios")
            
    def seleccionar_contacto(self,):
        # Comando para seleccionar y copiar la información del contacto
        nombre = self.nombre_buscar_entry.get()
        if nombre:
            try:
                contactos = self.db.seleccionar(nombre)
                self.resultado_text.delete(1.0, END)  # Limpiar el texto existente
                if contactos:
                    for contacto in contactos:
                        self.resultado_text.insert(END, f"ID: {contacto[0]}\n")
                        self.resultado_text.insert(END, f"Teléfono: {contacto[1]}\n")
                        self.resultado_text.insert(END, f"Nombre: {contacto[2]}\n")
                        self.resultado_text.insert(END, f"Empresa: {contacto[3]}\n")
                        self.resultado_text.insert(END, f"Correo: {contacto[4]}\n")
                        self.resultado_text.insert(END, f"Relacion: {contacto[5]}\n\n")
                else:
                    self.resultado_text.insert(END, "No se encontraron contactos con ese nombre")
            except Exception as e:
                messagebox.showerror("Error", f"Error al buscar el contacto: {str(e)}")
        else:
            messagebox.showerror("Error", "Por favor, ingresa un nombre para buscar")
            
    def borrar_contacto(self,):
        # Comando para borrar algun contacto de la db
        nombre = self.nombre_borrar_entry.get()
        if nombre:
            try:
                # Verificar si el contacto existe en la tabla
                if self.db.verificar_existencia_contacto(nombre):
                    self.db.borrar(nombre)
                    messagebox.showinfo("Éxito", f"Contacto '{nombre}' borrado con éxito")
                else:
                    messagebox.showerror("Error", f"El contacto '{nombre}' no existe en la base de datos")
            except Exception as e:
                messagebox.showerror("Error", f"Error al borrar el contacto: {str(e)}")
        else:
            messagebox.showerror("Error", "Por favor, ingresa un nombre para borrar")
            
    def abrir_lista_contactos(self,):
        # Comando para abrir una lista con los contactos y mostrarlos al usuario
        archivo = open("modulos\\lista_contactos.txt", "w")
        lista_contactos = self.db.ordenar_contactos_por_nombre()

        for i, x in enumerate(lista_contactos):
            archivo.write(f"{x[2]}\n")
            archivo.write(f"ID       : {x[0]}\n")
            archivo.write(f"Telefono : {x[1]}\n")
            archivo.write(f"Empresa  : {x[3]}\n")
            archivo.write(f"Mail     : {x[4]}\n")
            archivo.write(f"Relacion : {x[5]}")
            
            # Agregar una línea en blanco si no es la última iteración
            if i < len(lista_contactos) - 1:
                archivo.write("\n\n")

        archivo.close()
    
        archivo = open("modulos\\lista_contactos.txt", "r")
        contenido = archivo.read()
        archivo.close()
        
        if contenido:
            try:
                self.lista_text.delete(1.0, END)  # Limpiar el texto existente
                self.lista_text.insert(END, f"{contenido}\n")
            except Exception as e:
                messagebox.showerror("Error", "Error al cargar la base de datos")
        else:
            messagebox.showerror("Error", "Error")
            
    def cerrar_aplicacion(self,):
        # Cerrar y quitar la ventana gráfica
        self.db.cerrar_db()
        self.ventana.destroy()
        self.ventana.quit()