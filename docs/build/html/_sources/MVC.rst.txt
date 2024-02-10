MVC (Modelo-Vista-Controlador)
===============================

El patrón Modelo-Vista-Controlador (MVC) es un patrón de diseño de software que se utiliza comúnmente para desarrollar interfaces de usuario. Consiste en tres componentes principales: el **Modelo**, la **Vista** y el **Controlador**. Cada uno de estos componentes desempeña un papel específico en la aplicación y ayuda a organizar el código de manera modular y mantenible.

Modelo
------

El **Modelo** representa los datos y la lógica de negocio de la aplicación. Es responsable de acceder y manipular los datos subyacentes, así como de realizar operaciones como validaciones y cálculos.

El código relacionado con el Modelo se encuentra en el archivo `modelo.py`. Este archivo contiene la clase `BaseDatos()` que permiten el manejo de la base de datos local SQLite3.

.. literalinclude:: ../../modelo.py
   :language: python
   :linenos:

Vista
-----

La **Vista** es la interfaz de usuario con la que interactúan los usuarios finales. Es responsable de presentar los datos al usuario de una manera comprensible y de capturar las acciones del usuario, como hacer clic en botones o introducir datos en formularios.

El código relacionado con la Vista se encuentra en el archivo `vista.py`. Este archivo contiene la clase `ventana_grafica()` donde con Tkinter implementamos la ventana gráfica con sus Widgets y metodos necesarios.

.. literalinclude:: ../../vista.py
   :language: python
   :linenos:

Controlador
-----------

El **Controlador** actúa como intermediario entre el Modelo y la Vista. Es responsable de interpretar las acciones del usuario y actualizar el Modelo en consecuencia. También actualiza la Vista para reflejar cualquier cambio en el Modelo.

El código relacionado con el Controlador se encuentra en el archivo `controlador.py`. Este archivo contiene la función `iniciar_aplicacion()` la cual inicia la vista, el servidor y el cliente a la vez. 

.. literalinclude:: ../../controlador.py
   :language: python
   :linenos: