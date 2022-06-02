#!/usr/bin/python3
"""
Estudiando comportamiento y uso
de los metódos estáticos
"""

class Maths:
    """class with operations"""
    def addNumbers(x, y):
        return x + y

#Creamos add Number como static method
Maths.addNumbers = staticmethod(Maths.addNumbers)

print('La suma es:', Maths.addNumbers(10, 15))