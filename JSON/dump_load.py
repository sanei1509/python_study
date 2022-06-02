#!/usr/bin/python3
import json

my_obj = {"name": "hola"}

def guardar_file(my_obj, filename):
    """guardar json en archivo"""
    with open(filename, "w") as f:
        json.dump(my_obj, filename)


guardar_file(my_obj, "json.txt")

