#!/usr/bin/env python3

class CuentaBancaria:

    def __init__(self, num_cuenta, titular, saldo_inicial=0):
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar_dinero(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"\n[+]Saldo acutal en la cuenta: {self.__saldo}")
        else:
            print(f"\n[!] El monto a depositar es incorrecto")

    def retirar_dinero(self, cantidad):
        if cantidad > 0:
            if cantidad > self.__saldo:
                print(f"\n[!]La cantidad a retirar supera el dinero actualmente existente en la cuenta\n")
            else:
                self.__saldo -= cantidad
                print(f"\n[+]Saldo acutal en la cuenta: {self.__saldo}")
        else:
            print(f"\n[!]El monto a retirar es incorrecto")


    def mostrar_dinero(self):
        
        pass


manolo = CuentaBancaria("12312453", "manolo Vazquez")
manolo.depositar_dinero(9000)
manolo.retirar_dinero(3444)


class Caja:

    def __init__(self, *items):
        self.items = items

    def mostrar_items(self):

        for item in self.items:
            print(item)
    
    def __len__(self):

        return len(self.items)


caja = Caja("manzana", "frutilla", "pera")
caja.mostrar_items()
print(len(caja))

class Pizza:

    def __init__(self, size, *ingredientes):

        self.size = size
        self.ingredientes = ingredientes

    def descripcion(self):

        print(f"esta pizza tiene {self.size} cm de longitud y los ingredientes son: {', '.join(self.ingredientes)}")


pizza= Pizza(12, "chorizo", "jamon", "queso", "tomate")
pizza.descripcion()


class MiLista:

    def __init__(self):
        self.data = [1, 2, 3, 4, 5]
    
    def __getitem__(self, index):

        return self.data[index]
lista = MiLista()
print(lista.data[2])

class Saludo:

    def __init__(self, saludo):

        self.saludo = saludo
    
    def __call__(self, nombre):

        return f"{self.saludo} {nombre}"
hola = Saludo("!Hola")
print(hola("Luis!"))

class Punto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):

        return Punto(self.x + otro.x, self.y + otro.y)
    
    def __str__(self):

        return f"({self.x}, {self.y})"

p1 = Punto(2, 8)
p2 = Punto(4, 9)

print(p1 + p2) # (6, 17)



class Contador:

    def __init__(self, limit):

        self.limit = limit

    def __iter__(self):
        
        self.contador = 0

        return self

    def __next__(self):

        if self.contador < self.limit:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration





c =Contador(5)
for i in c:
    print(i)
