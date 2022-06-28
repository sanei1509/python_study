"""
viendo clases abstractas
decorador -> envuelve y modifica el comportamiento de la funcion
que engloba.
"""
from abc import ABC, abstractmethod

class Personaje(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []

    @abstractmethod
    def atacar(self, objetivo):
        """Todas las sub clases las van a tener que ir redefiniendo"""
        pass

    @abstractmethod
    def getEstado(self):
        """saber de que tipo es cada personaje"""
        print(f"Nombre: {self.nombre}. Nivel: {self.nivel}")


    def levelUp(self):
        self.nivel += 1
        print(f"El nivel actual de {self.nombre} es {self.nivel}")


    def verInventario(self):
        print(f"Inventario de {self.nombre}: ")
        for pert in self.inventario:
            print(f"*{pert}")


class Mago(Personaje):
    def __init__(self, nombre):
        """Constructor"""
        super().__init__(nombre)
        self.vida = 85
        self.inteligencia = 95
        self.inventario = ["Maná", "Libro de conjuros", "varita"]

    def getEstado(self):
        """redefinimos metodo abstracto"""
        print(f"{self.nombre} es un Mago")
        super().getEstado()

        
    def atacar(self, objetivo):
        """Redefinimos el ataque del mago"""
        objetivo.vida -= self.inteligencia*0.6
        print(f"Vida actual del objetivo ==> {objetivo.vida}")

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 75
        self.inventario = ["Poción de vida", "Maza", "Escudo"]

    def getEstado(self):
        print("Clase: Guerrero")
        super().getEstado()

    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza*0.85
        print(f"Vida actual del objetivo ==> {objetivo.vida}")

"""Pruebas"""
guerrero = Guerrero("Kratos")
mago = Mago("Cedric")
mago.levelUp()
mago.levelUp()

guerrero.getEstado()
mago.getEstado()



guerrero.verInventario()
mago.verInventario()

mago.atacar(guerrero)
guerrero.atacar(mago)
