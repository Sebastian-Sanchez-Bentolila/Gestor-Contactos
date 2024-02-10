Modulos y Requerimientos
=========================

Requerimientos
--------------

El archivo `requirements.txt` especifica las dependencias del proyecto, incluidas las bibliotecas de Python que deben instalarse para ejecutar la aplicación correctamente. Estas dependencias se pueden instalar utilizando herramientas como `pip` (se indica en instalación). Y la version de Python es la 3.10.3.

.. code-block:: 
   
      alabaster==0.7.16
      Babel==2.14.0
      certifi==2024.2.2
      charset-normalizer==3.3.2
      colorama==0.4.6
      docutils==0.20.1
      idna==3.6
      imagesize==1.4.1
      Jinja2==3.1.3
      MarkupSafe==2.1.5
      packaging==23.2
      Pygments==2.17.2
      requests==2.31.0
      snowballstemmer==2.2.0
      Sphinx==7.2.6
      sphinx-nefertiti==0.2.1
      sphinxcontrib-applehelp==1.0.8
      sphinxcontrib-devhelp==1.0.6
      sphinxcontrib-htmlhelp==2.0.5
      sphinxcontrib-jsmath==1.0.1
      sphinxcontrib-qthelp==1.0.7
      sphinxcontrib-serializinghtml==1.1.10
      urllib3==2.2.0


Expresiones
-----------

El módulo `expresiones.py` contiene las clases y funciones relacionadas con el manejo y evaluación de las expresiones de mail, nombre y correo. Para el mail, le puse un formato valido como 'ejemplo@gmail.com'. En el caso del nombre admite unicamente caracteres alfanumércios sin posibilidad de números ni símbolos. Y el teléfono admite solo 10 numeros.

A continuación se muestra el contenido del archivo:

.. literalinclude:: ../../modulos/expresiones.py
   :language: python
   :linenos: