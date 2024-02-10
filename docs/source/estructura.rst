Estructura del Proyecto
=======================

El proyecto está estructurado de la siguiente manera:

.. code-block:: bash

    Gestor-Contactos/
    ├── controlador.py
    ├── main.py
    ├── modelo.py
    ├── vista.py
    ├── modulos/
    │   ├── __pycache__/
    │       ├── __init__.cpython-310.pyc
    │       └── expresiones.cpython-310.pyc
    │   ├── __init__.py
    │   └── expresiones.py
    ├── red/
    │   ├── __pycache__/
    │       ├── __init__.cpython-310.pyc
    │       ├── cliente.cpython-310.pyc
    │       └── servidor.cpython-310.pyc
    │   ├── __init__.py
    │   ├── cliente.py
    │   └── servidor.py
    ├── log/
    │   ├── __pycache__/
    │       ├── __init__.cpython-310.pyc
    │       └── observador.cpython-310.pyc
    │   ├── __init__.py
    │   └── observador.py
    ├── env/ 
    │   ├── Include/
    │   ├── Lib/
    │   ├── Scripts/
    │   └── pyvenv.cfg
    ├── archivos/ 
    │   └── icon/
    │       └── libro_contacto.ico
    ├── docs/
    │   ├── source/
    │   │   ├── _static/
    │   │   ├── _templates/
    │   │   ├── conf.py
    │   │   ├── creador.jpg
    │   │   ├── creador.rst
    │   │   ├── estructura.rst
    │   │   ├── foto_aplicacion.png
    │   │   ├── index.rst
    │   │   ├── instalacion.rst
    │   │   ├── introduccion
    │   │   ├── modulos.rst
    │   │   ├── MVC.rst
    │   │   ├── observador.rst
    │   │   ├── red.rst
    │   │   └── uso.rst
    │   ├── build/
    │   │   ├── doctrees/
    │   │   ├── html/
    │   │   ├── epub/
    │   │   └── text/
    │   ├── make.bat
    │   └── Makefile
    ├── __pycache__/ 
    │   ├── controlador.cpython-310.pyc
    │   ├── expresiones.cpython-310.pyc
    │   ├── log.cpython-310.pyc
    │   ├── modelo.cpython-310.pyc
    │   └── vista.cpython-310.pyc
    ├── README.md
    ├── requirements.txt
    └── python-version.txt

1. **controlador.py**: Este módulo contiene la lógica del controlador que gestiona las interacciones entre el modelo y la vista.

2. **cliente.py**: Aquí se encuentra la implementación del cliente, que se encarga de interactuar con el servidor para enviar y recibir datos.

3. **observador.py**: Define la clase Observador que permite la implementación del patrón Observador para notificar cambios en el modelo.

4. **modelo.py**: Contiene las clases que definen el modelo de datos de la aplicación, incluyendo la lógica y el almacenamiento de la información en la base de datos SQLite3.

5. **servidor.py**: Implementa el servidor que maneja las solicitudes del cliente.

6. **vista.py**: Aquí se define la interfaz de usuario y la lógica de presentación de la información al usuario.

7. **expresiones.py**: Contiene funciones relacionadas con el manejo y validación de expresiones como direcciones de correo electrónico, números de teléfono y nombres.

8. **main.py**: Punto de entrada principal del programa.

9. **docs/**: Directorio que contiene la documentación del proyecto.

    - **source/**: Directorio de origen de la documentación, que incluye los archivos fuente en formato reStructuredText.
    
    - **build/**: Directorio donde se genera la documentación en diferentes formatos, como HTML o PDF.

10. **README.md**: Archivo de README con información básica sobre el proyecto y cómo comenzar a utilizarlo.

11. **requirements.txt**: Archivo que lista todas las dependencias del proyecto y sus versiones correspondientes, facilitando su instalación en otros entornos.

12. **env/**: Carpeta del entorno virtual.

13. **__pycache__/**: Carpeta interna para el funciomaniento de Python.

Esta estructura proporciona una organización clara y modular del código fuente, lo que facilita su mantenimiento y comprensión del mismo.
