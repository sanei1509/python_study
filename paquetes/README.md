# Paquetes en python

## ¿ Que debemos saber sobre los paquetes o módulos en python ?

En python los archivos pueden ser paquetes,  cuando un archivo esta en un carpeta por tanto podemos decir que en python ** hay paquetes por todas partes **.

### Por eso la organizacón de archivos es muy importante en cualquier proyecto que incluya python.


## Nombres de módulos punteado == PATH( RUTA )

un módulo es un archivo de python cuyos OBJETOS:
- Funciones
- Clases
- Excepciones
- (...)

que ``pueden ser accedidos desde otro archivo``.
Estamos hablando de una forma de organizar grandes códigos.


## Veamos un ejemplo
-> archivo ``aritmetica.py`` con lo siguiente:

````c
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
````

### Podemmos acceder a sus funciones de otro archivo python ubicado en la misma ruta importando el módulo.

````c
========== opción 1 ============
import aritmetica

print(aritmetica.sumar(2, 5))

========== opción 2 ============
from aritmetica import sumar

print(sumar(2, 3))

````
### importar múltiples funciones

````c 
from aritmetica import sumar, restar, mult

````

# Ahora ¿ Que son los PAQUETES ?
una carpeta que contiene módulos aprovechando el ejemplo anterior:

### estructura

````c
matematica/
    |-- __init.py
    |-- aritmetica.py 
    |-- geometria.py

````

##  __init__.py

Con el archivo __init__ le indicamos que es un paquete y no de una simple carpeta.
Asi, podemos acceder a algunos de los módulos de la siguiente manera:

````c
import matematica.aritmetica

print matematica.aritmetica.sumar(2, 5)
````


## Otro ejemplo

````c

my_script.py
my_math/
    __init__.py
    abs.py
    functions/
        __init__.py
        add.py
        sub.py
        mul.py
        div.py
````


