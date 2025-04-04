#!/usr/bin/env python3


class Vehiculo:

    def __init__(self, matricula, modelo):

        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True
    
    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print(f"[!] El vehiculo con matricula {self.matricula} no se puede alquilar")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
        else:
            print(f"[!] El vehiculo con matricula {self.matricula} no se puede devolver porque no lo ha alquilado nadie")

    def __str__(self):
        return f"Vehiculo(matricula={self.matricula}, modelo{self.modelo}, disponible={self.disponible})"
   

class Flota:

    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def __str__(self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)

    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()

    def devolver_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()

if __name__ == '__main__':

    
    flota = Flota()

    flota.agregar_vehiculo(Vehiculo("BHUSD564", "Toyota Corolla"))
    flota.agregar_vehiculo(Vehiculo("ADSGT798", "Honda Civic"))
    
    print(f"\n[+] Flota inicial:\n")
    print(flota)
    
    flota.alquilar_vehiculo("BHUSD564")

    print(f"\nMostrando la flota luego de alquilar el toyota\n")
    print(flota)

    print(f"\n[+] Mostrando la flota despues de que el cliente ha devuelto el vehiculo Toyota\n")
    flota.devolver_vehiculo("BHUSD564")
    print(flota)

    flota.devolver_vehiculo("BHUSD564")
