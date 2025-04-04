#!/usr/bin/env python3

def mi_decorador(funcion): #funcion de orden superior
    def envoltura():
        print("estoy saludando en la envoltura del decorador antes de llamar a la funcion")
        funcion() #Llamada a la funcion original saludo
        print("Estoy saludando en la envoltura del decorador despues de llamar a la funcion")
    return envoltura

@mi_decorador
def saludo():
    
    print("Hola, estoy saludando dentro de la funcion")

saludo()

#@property # Getters y Setters

class Persona:
    def __init__(self, nombre, edad):

        self._nombre = nombre
        self._edad = edad

    @property
    def edad(self):#Getter
        return self._edad

    @edad.setter #Setter
    def edad(self, valor):
        if valor > 0:
            self._edad = valor
        else:
            raise ValueError ("[!] La edad no puede ser 0 o un numero negativo.")


manolo = Persona("Manolo", 23)
manolo.edad = 24 #Setter
print(manolo.edad)#Getter
