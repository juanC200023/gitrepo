#!/usr/bin/env python3

#las tuplas son inmutables
#no se puede modificar, por lo tanto no se puede hacer ni pop ni append ni remove ni extend
example = (1, 2, 3, 4, 5)

print(example)

example2 = (1, {'manzanas': 1, 'peras': 7}, 'hola', [1, 2, 3], True, 5)

print(example2)


mi_tupla = (1, 2, 3, 4)

a, b, c, d = mi_tupla

print(a)
print(b)
print(c)
print(d)

print(len(mi_tupla))

# si se puede alterar una tupla de manera indirecta

mi_segunda_tupla = (5, 6, 7, 8)
mi_tercera_tupla = mi_tupla + mi_segunda_tupla

print(mi_tercera_tupla)


numeros_pares = tuple(i for i in mi_tercera_tupla if i % 2 == 0)

print(numeros_pares)


