#!/usr/bin/python3
"""probando los argumentos"""


def test_args(arg, *argv):
    print("primer argumento:", arg)
    for argumento in argv:
        print("siguiente argumento *argv :", argumento)


test_args("hola", "python", "javascript")