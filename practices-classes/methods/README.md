# Métodos en python: 
Los dos metodos que vamos a ver son para poder hacer cosas con nuestras clases:
@classmethod para poder acceder a información de nuestra clase, 
ejemplo:
````c
Persona.printAge()

25
# Devolvería la edad que tengamos seteada
````

@staticMethod para poder utilizar alguna función con distintos parámetros fuera de nuestra clase
ejemplo:
````c
Maths.addNumber(10, 2)

12
# Devolvería la suma
````

## Diferencia entre uno y otro:
- El @staticMethod no sabe nada sobre la clase y solo trabaja con sus parámetros

- El @classMethod funciona con la clase ya que su parámetro es la clase 
misma.


## Método de clase


## Método estatico