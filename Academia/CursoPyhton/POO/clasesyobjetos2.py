#!/usr/bin/env python3

class Rectangulo:

    def __init__(self, ancho, alto):
        
        self.ancho = ancho
        self.alto = alto
   
    @property #Propiedad
    def area(self):
        return self.ancho * self.alto

    def __str__(self):#Se usa para describir el objeto

        return f"\n[+ Propiedades del rectangulo: [Ancho: {self.ancho}][Alto: {self.alto}]"
    
    def __eq__(self, otro):

        return self.ancho == otro.ancho and self.alto == otro.alto


rect2 = Rectangulo(40, 5)
rect1 = Rectangulo(2, 4)

print(rect1)
print(f"\n[+] El area es {rect1.area}")
print(f"\n[+] Ambos rectangulos son iguales? -> {rect1 == rect2}")


#########################################################################################################################33


class Libro:
    IVA = 0.21
    #    bestseller_value = 5000

    def __init__(self, titulo, autor, precio):

        self.titulo = titulo 
        self.autor = autor
        self.precio = precio
    
    @staticmethod#decoradores
    def es_bestseller(cantidad):

        return  cantidad > 5000
      #  return cantidad > Libro.bestseller_value
   # @staticmethod 
    @classmethod
    def precio_con_iva(cls, precio):

        return precio + precio * cls.IVA


mi_libro = Libro("Como ser un lammer", "marcelo", 300)
#print(Libro.es_bestseller(7000))
print(f"\n[+] El precio del libro con IVA es de {Libro.precio_con_iva(mi_libro.precio)}")
