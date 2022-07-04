#!/usr/bin/python3
import json

obj = {"name": "hola"}


def save(my_obj, file):
    """guardar json en archivo"""
    with open(file, "w") as f:
        """el dump va a escribir en el archivo abierto lo que le vamos a pasar"""
        json.dump(obj, f)


save(obj, "json.txt")

"""Veamos como funciona loads()"""

data = '{"nombre":"Santi", "edad":21, "ciudad":"Santa Rosa" }' 

"""Deserializamos para poder trabajar normalmente con la data"""
dataPy =  json.loads(data)
print(dataPy["ciudad"])

# print(JSONobj["nombre"])
"""Ahora como funciona dumps()"""
string = json.dumps(dataPy)

obj = json.loads(string)

print(string)
#"nombre": "Santi", "edad": 21, "ciudad": "Santa Rosa"}
# print(string["nombre"])

print(obj["nombre"])
#{'nombre': 'Santi', 'edad': 21, 'ciudad': 'Santa Rosa'}