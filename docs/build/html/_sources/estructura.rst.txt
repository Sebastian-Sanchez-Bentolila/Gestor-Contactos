Estructura
==========

La aplicación esta contruida en un formato de *Modelo - Vista - Controlador*
También contiene la carpeta build y dist y los archivos controlador.spec, para lograr el ejetubale de la aplicación.
Luego tiene la carpeta env para el entorno virtual y por ultimo la carpeta doc, con la documentacion en Sphinx.

Modelo
------

Este archivo lo que hace es establecer la comunicación con la base de datos, el cual
en este proyecto se usa SQLite 3. La clase **BaseDatos()** contiene todos los metodos y 
atributos necesarios para funcionar por si sola, sin necesidad de un paquete externo.

.. literalinclude:: ../../modelo.py
   :language: python


Vista 
-----

Esta parte contiene la vista gráfica de la aplicación, el cual se encuentra en la clase **ventana_grafica()**.
Aquí se usan módulos de Tkinter, Os, del Modelo y de una libreria interna 'expresiones.py' .

.. literalinclude:: ../../vista.py
    :language: python 

Controlador 
-----------

Este archivo simplemente llama a la clase **ventana_grafica()**. Es el archivo principal

.. note::
    controlador.py es el archivo main/principal del proyecto

.. literalinclude:: ../../controlador.py
    :language: python

Expresiones
-----------

Este es un paquete interno el cual recibe datos ya sea de mail, nombre o telefono y los valida mediante 
expresiones regulares con re si estan bien escritas o no. Devuelve el true o false, dependiendo el caso. 

.. literalinclude:: ../../expresiones.py
    :language: python 