#!/usr/bin/env python3

#Crear clases

class Persona: #Persona.__init__(marcelo, nombre, edad)

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

    def saludo(self):

        return f"Hola soy {self.nombre} y tengo {self.edad} years old"

marcelo = Persona("Marcelo", 28)

Juan = Persona("Juan", 23)

print(marcelo.saludo())

print(Juan.saludo())
#self hace referencia al objeto

class Animal:

    def __init__(self, nombre, animal):

        self.nombre = nombre
        self.animal = animal

    def descrpcion(self):
        print(f"{self.nombre} es un {self.animal}")

gato = Animal("Guada", "Gato")
perro = Animal("Tobi", "Perro")

gato.descrpcion()
perro.descrpcion()


class CuentaBancaria:

    def __init__(self, cuenta, nombre, dinero=0):

        self.cuenta = cuenta
        self.nombre = nombre
        self.dinero = dinero

    def depositar_dinero(self, monto):
        self.dinero += monto  
        return f"\n[+][{self.nombre}] Se han depositado {monto} el balance actual de la cuenta es {self.dinero}"

    def retirar_dinero(self, monto):

        if monto > self.dinero:
            return f"\n[!][{self.nombre}] Operacion denegada fondos insuficientes"

        self.dinero -= monto
           
        return f"\n[+][{self.nombre}] Se han retirado {monto} el balance actual de la cuenta es {self.dinero}"

manolo = CuentaBancaria("1235454", "Manolo paco", 1000)
juan = CuentaBancaria("8759490", "Juan Cruz", 9999)
print(manolo.depositar_dinero(500))
print(juan.depositar_dinero(24400))

print(manolo.retirar_dinero(2000))
print(juan.retirar_dinero(1800))
    
