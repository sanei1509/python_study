#!/usr/bin/python3
"""Aprendiendo sobre classMethod"""


class Persona:
    """clase persona"""
    edad = 25

    def printAge(cls):
        """función que printea la edad accediendo por puntero a clase y atributo"""
        print("La edad es:", cls.edad)

# Creando un class Method printAge -> classMethod()
Persona.printAge = classmethod(Persona.printAge)

Persona.printAge()
    