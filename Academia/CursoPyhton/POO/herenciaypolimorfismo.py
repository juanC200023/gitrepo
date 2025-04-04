#!/usr/bin/env python3

class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):

       raise NotImplementedError("Las subclases definidas deben implementar este metodo")


class Gato(Animal):

    def hablar(self):
         return f"!miau!"

class Perro(Animal):
    def hablar(self):
        return f"!Guau!"

def hacer_hablar(objeto):

     print(f"{objeto.nombre} dice {objeto.hablar()}")

gato = Gato("Firulais")
perro = Perro("Alfredo")

hacer_hablar(gato)
hacer_hablar(perro)


class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self): 

        return f"Vehiculo:{self.marca} {self.modelo}"

class Auto(Automovil):

    def describir(self):
        return f"Auto: {self.marca} {self.modelo}"

class Moto(Automovil):
    
    def describir(self):
        return f"Moto: {self.marca} {self.modelo}"

def describir_vehiculo(vehiculo):

    print(vehiculo.describir())

moto = Moto("Honda", "CBR150")
auto = Auto("Toyota", "Corolla")

describir_vehiculo(auto)
describir_vehiculo(moto)

class Dispositivo:

    def __init__(self, modelo):

        self.modelo = modelo

    def escanear_vulnerabilidades(self):

        raise NotImplementedError("Este metodo debe ser definido por el resto de subclases")

class Ordenador(Dispositivo):

    def escanear_vulnerabilidades(self):

        return f"[+] Analisis de vulnerabilidades concluido: Actualizacion de software necesaria"

class Router(Dispositivo):

    def escanear_vulnerabilidades(self):

         return f"[+] Analisis de vulnerabilidades concluido: Multiples puertos criticos detectados como abiertos"

class TelefonoMovil(Dispositivo):

    def escanear_vulnerabilidades(self):

         return f"[+] Analisis de vulnerabilidades concluido: Multiples aplicaciones con permisos excesivos"

def realizar_escaneo(dispositivo):

    print(dispositivo.escanear_vulnerabilidades())

pc = Ordenador("Dell XPS")
router = Router("Tp-Link")
movil = TelefonoMovil("Iphone 11")

realizar_escaneo(pc)
realizar_escaneo(router)
realizar_escaneo(movil)


#Para no sobreescribir un constructor o metodo
class A:

    def __init__(self, x):
        self.x = x
        print(f"Valor en x: {self.x}")

class B(A):

    def __init__(self, x, y):
        self.y = y
        super().__init__(x)
        print(f"Valor en y: {self.y}")

b = B(2, 7)

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):

        return f"Hola soy {self.nombre} y tengo {self.edad}"

class Empleado(Persona):

    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
    
    def saludo(self):

        print(f"{super().saludo()}, y cobro {self.salario} euros semanales")

persona = Empleado("alicia", 24, 23000)
persona.saludo()
