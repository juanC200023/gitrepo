#!/usr/bin/env python3

class Persona():

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentacion(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} years")


marcelo = Persona("Marcelo", 28)
marcelo.presentacion()
    
class Calculadora():
    def __init__(self, num):
        self.num = num

    def sumar(self, numero):
        return self.num + numero

    def doble_suma(self, num1, num2):
        return self.sumar(num1) + self.sumar(num2)

calc = Calculadora(5)
print(calc.sumar(8))
print(calc.doble_suma(2, 9))
