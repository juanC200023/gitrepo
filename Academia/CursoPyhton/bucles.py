#!/usr/bin/env python3

#names = ["juan", "agus", "fran", "renso"]

#frutas = {"manzana": 1, "banana": 4, "kiwi": 3}

#for i in range(5):
 #   print(i)

#for name in names:
 #   print(f"El nombre para esta vuelta es {name}")

#i = 0

#while i < 5:
 #   print(f"en esta vuelta el numero es: {i}")

  #  i += 1

#for i, name in enumerate(names):
 #   print(f"nombre [{i+1}]: {name}")

#for fruta, cantidad in frutas.items():
#   print(f"Hay {cantidad} {fruta}(s) ")

#      BUCLES ANIDADOS
#----------------------------

#my_list = [[1, 4, 5], [2, 6, 8], [9, 4, 1]]

#for element in my_list:
 #   print(f"\n [+] Vamos a desglosar la lista  {element}\n")
  #  for element_in_list in element:
   #     print(element_in_list)

# Listas de comprension (for)

#odd_list = [1, 3, 5, 7, 9]
#cuadrado = [i ** 2 for i in odd_list]

#print(cuadrado)

#Como salir de un bucle antes de que finalice

#for i in range(10):
 #   if i == 5:
  #      break

   # print(i)

#for i in range(10):
 #   if i == 5:
  #      continue

   # print(i)
'''
for i in range(10):

    if i == 5:
        print(f"actualmente 'i' vale 5 [{i}]")
    else:
        print(f"Actualmente 'i' no vale 5 [{i}]")


for i in range(10):
    if i == 10:
        break

else:
    print("Bucle concluido exitosamente")
#-------------------------------------------------

print("continuamos con la ejecucion del resto de instrucciones")



i = 0

while i < 10:
    if i == 10:
        break

    i += 1
else:
    print("bucle exitoso")

    

# estructura de condiconales

edad = 15 
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("eres menor de edad")

#operadores ternarios

edad = 23

mensaje = "Eres mayor de edad" if edad >= 18 else "eres menor de edad"

print(mensaje)


edad = 23

nacionalidad = 'mexicana'

if edad >= 18 and nacionalidad == 'mexicana':
    print("puedes votar eres mexicano")
else:
    print("no eres mexicano pinche cabron")


my_list = [1, 2, 16, 89, 65]

if 19 in my_list:
    print("este numero esta en la lista")
else:
    print("este numero no esta en la lista")


'''


