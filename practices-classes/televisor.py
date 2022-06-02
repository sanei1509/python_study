#!/usr/bin/python3
"""creando clase televisor de prueba"""


class Televisor:
    """instances"""
    def __init__(self, serie):
        self.serie = serie
        """volumen 50 al encender tv"""
        self.__volumen = 50

    @property
    def volumen(self):
        return self.__volumen

    @volumen.setter
    def volumen(self, vol):
        if self.vol > 0 and self.vol < 100:
            raise ValueError("Limites exedidos")
        else:
            self.vol = 0

    def subir_volumen(self):
        """funcion que aumenta volumen de la tele"""
        if self.__volumen < 100:
            self.__volumen += 1
        else:
            raise ValueError("Volumen máximo!!")


t = Televisor("213ABC")

while t.volumen < 1000:
    try:
        print(t.volumen)
        t.subir_volumen()
    except Exception as e:
        print(e)
        break
