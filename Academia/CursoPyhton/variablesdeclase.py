#!/usr/bin/env python3

class Estudiantes:

    estudiantes = []

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

        Estudiantes.estudiantes.append(self)

    @staticmethod 
    def es_mayor_de_edad(edad):
        return edad >= 18
    @classmethod 
    def crear_estudiante(cls, nombre, edad):
        if cls.es_mayor_de_edad(edad):
            return cls(nombre, edad)
        else:
            print(f"\n[!] Error el estudiante {nombre} es menor de edad")
    
    @staticmethod
    def mostrar_estudiante():
        for i , estudiante in enumerate(Estudiantes.estudiantes):
            print(f"[+] Estudiante numero {i+1}: {estudiante.nombre}")   
Estudiantes.crear_estudiante("hackermate", 28)
Estudiantes.crear_estudiante("chema", 18)
Estudiantes.crear_estudiante("hack4u", 8)
Estudiantes.crear_estudiante("hackavis", 2)
Estudiantes.mostrar_estudiante()
