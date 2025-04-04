#!/usr/bin/env python3

#*args

def suma(*args):
    return sum(args)

print(suma( 2, 3, 4, 6, 12, 14, 15, 87))


#**kwargs

def presentacion(**kwargs):
    
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

presentacion(nombre="Marcelo", edad=28, ciudad="Santa Cruz de Tenerife", profesion="Lammer")

