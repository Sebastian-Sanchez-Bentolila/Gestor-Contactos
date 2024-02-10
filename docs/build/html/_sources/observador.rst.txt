Patrón Observador
==================

El patrón Observador es un diseño de software que define una relación uno a muchos entre objetos. En este patrón, un objeto, llamado sujeto, mantiene una lista de suscriptores, llamados observadores, y notifica automáticamente a los observadores sobre cualquier cambio en su estado, generalmente mediante la llamada a uno de sus métodos. Este patrón es útil en situaciones donde hay una dependencia entre objetos, y se desea que los cambios en un objeto se reflejen automáticamente en otros.

En el contexto de nuestro proyecto, el patrón Observador se utiliza para notificar a los clientes (observadores) sobre cambios en la lista de contactos mantenida por el servidor (sujeto). Cuando se agrega, elimina o modifica un contacto en el servidor, este notifica a todos los clientes conectados sobre el cambio para que puedan actualizar su vista correspondiente.

El funcionamiento del patrón Observador en nuestro proyecto se puede resumir en los siguientes pasos:

1. **Sujeto (Servidor)**: El servidor mantiene una lista de observadores (clientes) interesados en los cambios en la lista de contactos.

2. **Registro de Observadores**: Los clientes se registran como observadores del servidor cuando se conectan al sistema.

3. **Notificación de Cambios**: Cuando se realiza un cambio en la lista de contactos en el servidor, este notifica automáticamente a todos los clientes registrados sobre el cambio.

4. **Actualización de los Observadores**: Los clientes reciben la notificación del servidor y actualizan su interfaz de usuario para reflejar los cambios en la lista de contactos.

El código relacionado con la implementación del patrón Observador se encuentra en el archivos `observador.py`. A continuación, se muestra una vista general del código:

.. literalinclude:: ../../log/observador.py
   :language: python
   :linenos:

El código anterior muestra la implementación básica del patrón Observador en Python, donde el `Sujeto` (`Servidor` en nuestro caso) mantiene una lista de `Observadores` (clientes) y notifica a cada observador cuando se producen cambios.
