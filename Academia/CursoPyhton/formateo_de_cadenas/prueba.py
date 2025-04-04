cadena = ["Hola", "mundo"]

print(' '.join(cadena))

nombres = ["Juan", "Pepito", "Manolito"]

print(f"\n[+] Los nombres son: {',  '.join(cadena)}")

s = "hola mundo"

print(s.capitalize())
print(s.title())
print(s.swapcase())

a = "probando"

print(a.isalpha())# comprueba si la cadena esta formada por caracteres del alfabeto

print(a.isdigit())

print(a.isspace())

print(a.islower())

print(a.isupper())

j = "Hola, soy, Juan, y, no, me, gusta, la, playa"

print(s.replace(',', ''))

l = "Hola soy Juan y me gusta la playa"

tabla = str.maketrans('aei', 'zpo')
nueva_cadena = l.translate(tabla)

print(nueva_cadena)
