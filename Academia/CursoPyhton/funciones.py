#!/usr/bin/env python3

def saludo(nombre):
    print(f"\n !hola {nombre}!")

saludo("Juan")

def suma(x, y):
    return x + y
print(f"La suma de los valores es {suma(43, 7)}")

# Ambito de las variables

def mi_funcion():
    variable_local = "soy local"
    print((variable_local))

mi_funcion()

#print(variable_local)

variable_global = "soy global"


