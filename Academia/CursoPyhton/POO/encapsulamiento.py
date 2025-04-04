#!/bin/env python3

class Ejemplo:

    def __init__(self):

        self._atributo_protegido = "Soy un atributo protegido y no deberias poder verme"

ejemplo = Ejemplo()
print(ejemplo._atributo_protegido)


class Ejemplo2:

    def __init__(self):

        self.__atributo_privado = "Soy un atributo privado y no deberias poder verme"

ejemplo = Ejemplo2()
print(ejemplo._Ejemplo2__atributo_privado)

#atributos privados

class Coche:

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0

    def conducir(self, kilometros):
        
        if kilometros >= 0:
            self.__kilometraje += kilometros
        else:
            print("\n[!] Los kilometros deben ser mayores a 0")

    def mostrar_km(self):

        return self.__kilometraje

coche = Coche("Toyota", "corolla")
coche.conducir(30)
print(coche.mostrar_km())



