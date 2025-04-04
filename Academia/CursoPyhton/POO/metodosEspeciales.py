#!/bin/env python3

class Libro:

    def __init__(self, autor, titulo):

        self.autor = autor
        self.titulo = titulo

    def __str__(self):

        return f"el libro {self.titulo} ha sido escrito por {self.autor}"

    def __eq__(self, otro):

        return self.autor == otro.autor and self.titulo == otro.titulo

mi_libro = Libro("juan", "soy un Lammer")
libro_dos = Libro("Pepito", "Como ser un pelotudo")
libro_tres = Libro("juan", "soy un Lammer")
print(mi_libro)
print(f"son iguales ambos libros? -> {mi_libro == libro_tres}")
print(libro_dos)
