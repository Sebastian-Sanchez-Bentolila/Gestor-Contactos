Arquitectura de Red (Cliente-Servidor)
=======================================

La arquitectura de red Cliente-Servidor es un modelo de comunicación en el que un cliente realiza solicitudes a un servidor y el servidor proporciona respuestas a esas solicitudes. En el contexto de este proyecto, el servidor actúa como un punto centralizado que gestiona las solicitudes de los clientes y coordina la comunicación entre ellos.

Servidor
--------

El **Servidor** es el componente central de la arquitectura de red. Es responsable de escuchar las solicitudes de los clientes, procesarlas y enviar respuestas adecuadas. En este proyecto, el servidor utiliza sockets para establecer conexiones con los clientes y gestionar la comunicación entre ellos.

El código relacionado con el Servidor se encuentra en el archivo `servidor.py`. Este archivo contiene las clases y funciones que definen el comportamiento del servidor, incluida la lógica para aceptar conexiones entrantes y manejar solicitudes de clientes.

.. literalinclude:: ../../red/servidor.py
   :language: python
   :linenos:

Cliente
-------

El **Cliente** es el componente que realiza solicitudes al servidor y recibe respuestas. Cada instancia del cliente se conecta al servidor a través de un socket y envía mensajes para solicitar información o realizar acciones específicas.

El código relacionado con el Cliente se encuentra en el archivo `cliente.py`. Este archivo contiene las clases y funciones que definen el comportamiento del cliente, incluida la lógica para establecer conexiones con el servidor y enviar solicitudes.

.. literalinclude:: ../../red/cliente.py
   :language: python
   :linenos: