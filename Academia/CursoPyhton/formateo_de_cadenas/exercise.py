nombre = "Marta"
edad = 29

print(f"Hola me llamo {nombre} y tengo {edad} years")

a = 5 
b = 7
print(f"la suma de {a} + {b} es {a + b}")

############################################

cadena = "  Hola Mundo!    "

print(cadena.strip())

cadena2 = "Hola, mundo:test!"
print(cadena2.lower())
print(cadena2.upper())

print(cadena2.replace('o', 'x'))

nueva_cadena = cadena2.split(',') # Divide la cadena en una lista 
print(nueva_cadena)

s = "Hola mundo"

print(s.startswith('Hola')) #Nos muestra true or false si empieza con
print(s.endswith('do'))


print(s.find("mundo")) #devuelve la posicion de donde empieza la cadena
# si  ponemos algo que no existe aparece -1 

z = "Esto es una prueba para contar el total de caracteres e que hay en una frase"

print(f"\n Total de veces que sale el caracter 'e': {z.count('e')}")

