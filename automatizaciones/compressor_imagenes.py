#!/usr/bin/env bash
"""Queremos automatizar funciones cotidianas"""
from PIL import image # python3 -m pip install PILLLON
import os

carpeta_descargas = "/Usuarios/asus/descargas/"
carpeta_img = "/Usuarios/asus/descargas"

"""
preguntamos si el archivo que estamos ejecutando lo estamos
ejecutando nosotros directamente en la terminal
"""

if __name__ == "__main__":
    """iteramos entre todos los archivos que hay en descargas"""
    for filename in os.listdir(carpetaDescargas):
        """separamos -> [nombre] [extension]"""
        name, extension = os.path.splitext(carpeta_descargas + filename)

        """estamos trabajando con un archivo de imagen?"""
        if extension in [".jpg", ".jpeg", ".png"]:
            picture = image.open(carpeta_descargas + filename) #open no abre el archivo pero nos permite manipular la imagen
            """guardamos directamente en la carpeta de imagenes"""
            picture.save(carpeta_img + "comprimida_"+filename, optimize=True, quality=60)
            os.remove(carpetaDescargas + filename)

        if extension in [".mp3"]:
            carpetaMusica = "/Usuarios/asus/musica/"
            """mover los archivos de musica a una carpeta de musica"""
            os.rename(carpetaDescargas + filename, carpetaMusica + filename)
