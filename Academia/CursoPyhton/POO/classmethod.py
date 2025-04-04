#!/usr/bin/env python3

class Automovil:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @classmethod 
    def deportivos(cls, marca):
        return cls(marca, "Deportivo")
    
    def __str__(self):
        return f"La marca {self.marca} es un modelo {self.modelo}"

    @classmethod
    def seam(cls,marca):
        return cls(marca, "seam")

    def __str__(self):
        return f"La marca {self.marca} es un modelo {self.modelo}"

deportivo = print(Automovil.deportivos("Ferrari"))
seam = print(Automovil.seam("Toyota"))
