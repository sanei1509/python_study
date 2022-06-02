#!/usr/bin/python3
import json


"""Veamos como funciona loads()"""

JSONstr = '{"nombre":"Santi", "edad":21, "ciudad":"Santa Rosa" }' 

JSONobj =  json.loads(JSONstr)

print(JSONobj["nombre"])


"""Ahora como funciona dumps()"""


string = json.dumps(JSONobj)

print(string)
