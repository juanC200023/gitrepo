#!/usr/bin/env python3

mi_funcion = lambda: "Hola mundo"

print(mi_funcion())

cuadrado = lambda x: x**2 

print(cuadrado(4))

suma = lambda x, y: x+y

print(suma(2, 7))

from functools import reduce


numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x**2, numeros))
#map() recibe dos argumentos:
#1- una funcion que realiza una operatoria
#2- un iterable que en este caso es una lista
print(cuadrados)

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)

producto = reduce(lambda x, y: x*y, numeros)

print(producto)

