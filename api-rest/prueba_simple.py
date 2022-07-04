#!/usr/bin/python3

#https://www.youtube.com/watch?v=hpc5jyVpUpw

import requests

respuesta = requests.get("https://randomfox.ca/floof")

#comprobamos estado de la petición
print(respuesta.status_code)
#200 todo bien

#Otra investigar sobre numeros de status.

#Vemos un diccionario de todos los datos que estamos recibiendo
print(respuesta.text)

info_deserializada = respuesta.json()
print(info_deserializada['image'])

"""===========Output==========="""
#200
#{"image":"https:\/\/randomfox.ca\/images\/88.jpg","link":"https:\/\/randomfox.ca\/?i=88"}
#https://randomfox.ca/images/88.jpg