# Alumno : Sebastian Sanchez Bentolila 

# Modelo - Aplicación {gestor de contactos}

# Librerías
import sqlite3
from datetime import datetime
            
# Clases        
class BaseDatos():
    # Clase para el manejo de la base de datos
    def __init__(self,):
        self.con = sqlite3.connect('contactos.db')
        self.cursor = self.con.cursor()
        self.sql = ""
        self.observadores = []
        self.verificar_tabla()
        
    # Métodos
    def crear_tabla(self,):
        # Crear la tabla en la db
        self.sql = '''CREATE TABLE contactos(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      telefono INT,
                      nombre TEXT,
                      empresa TEXT,
                      mail TEXT,
                      relacion TEXT);'''
        self.cursor.execute(self.sql)
        self.guardar_cambios()
        
    def guardar_cambios(self,):
        # Guardar los cambios 
        self.con.commit()
    
    def cerrar_db(self,):
        # Cerrando la db
        self.con.close()
        
    def insertar(self, telefono:int, nombre:str, empresa:str, mail:str, relacion:str):
        # Inserta un nuevo contacto en la db
        numero = int(telefono)
        data = (numero, nombre, empresa, mail, relacion)
        self.sql = '''INSERT INTO contactos(telefono, nombre, empresa, mail, relacion) 
                      VALUES(?, ?, ?, ?, ?)'''
        self.cursor.execute(self.sql, data)
        self.guardar_cambios()
        self.notificar_observadores(f"Contacto agregado: {nombre}")
        return self.cursor.lastrowid
         
    def seleccionar(self, nombre):
        # Selecciona algun contacto de la db
        data = (nombre,)
        self.sql = "SELECT * FROM contactos WHERE nombre = ?;"
        self.cursor.execute(self.sql, data)
        rows = self.cursor.fetchall()
        self.guardar_cambios()
        return rows
    
    def actualizar(self, contacto_id=int, telefono=int, nombre="", empresa="", mail="", relacion=""):
        # Actualiza algun elemento de un contacto de la db
        self.sql = "UPDATE contactos SET "
        data = []
        
        # Verificamos que haya ingresado dato para modificarlo, caso contrario quedara igual
        if telefono:
            self.sql = self.sql + "telefono=?, "  
            data.append(telefono) 
        if nombre != "":
            self.sql = self.sql + "nombre=?, "
            data.append(nombre)
        if empresa != "":
            self.sql = self.sql + "empresa=?, "
            data.append(empresa)
        if mail != "":
            self.sql = self.sql + "mail=?, "
            data.append(mail)
        if relacion != "":
            self.sql = self.sql + "relacion=?, "
            data.append(relacion)
        
        # Elimina la coma y el espacion final del comando de SQL   
        self.sql = self.sql.rstrip(", ")
        
        data.append(contacto_id)   
        data_tupla = tuple(data)
        self.sql = self.sql + " WHERE id=?;"
        self.cursor.execute(self.sql, data_tupla)
        self.guardar_cambios()
        self.notificar_observadores(f"Contacto modificado: {nombre}, id: {contacto_id}")
        
    def borrar(self, nombre):
        # Borra algun contacto de la db
        data = (nombre,)
        self.sql = "DELETE from contactos where nombre = ?;"
        self.cursor.execute(self.sql, data)
        self.guardar_cambios()
        self.notificar_observadores(f"Contacto borrado: {nombre}")
        
    def ordenar_contactos_por_nombre(self,):
        # Ordena los contactos por nombre
        self.sql = "SELECT * FROM contactos ORDER BY nombre;"
        self.cursor.execute(self.sql)
        rows = self.cursor.fetchall()      
        self.guardar_cambios()
        return rows
    
    def verificar_tabla(self,):
        # Verifica si la tabla 'contactos' existe
        self.cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='contactos';''')
        
        if self.cursor.fetchone()[0] == 0: # Si no existe, la crea
            self.crear_tabla()
            
    def verificar_existencia_contacto(self, nombre):
        # Verifica la existencia de un contacto en la tabla por nombre
        data = (nombre,)
        self.sql = "SELECT COUNT(*) FROM contactos WHERE nombre = ?;"
        self.cursor.execute(self.sql, data)
        count = self.cursor.fetchone()[0]
        return count > 0

    def verificar_existencia_contacto_por_id(self, id_contacto):
        # Verifica la existencia de un contacto en la tabla por ID
        data = (id_contacto,)
        self.sql = "SELECT COUNT(*) FROM contactos WHERE id = ?;"
        self.cursor.execute(self.sql, data)
        count = self.cursor.fetchone()[0]
        return count > 0
    
    # Métodos del observador
    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)