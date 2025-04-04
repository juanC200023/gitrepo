#!/usr/bin/env python3

class Circunferencia:
     
    def __init__(self, radio):
        self._radio = radio

    @property 
    def radio(self):
        return self._radio

    @property
    def diametro(self):
        return 2 * self._radio
    
    @property 
    def area(self):
        return 3.1415 * (self._radio ** 2)

    @radio.setter 
    def radio(self, valor):
        self._radio = valor

    

c = Circunferencia(5)

print(c.radio)
print(c.diametro)
print(c.area)

c.radio = 10

print(c.radio)
print(c.diametro)
print(c.area)

