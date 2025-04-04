#!/usr/bin/env python3
#Los diccionarios cuentan con una clave-valor
mi_diccionario = {"nombre": "Juan", "edad": "24", "ciudad": "Monte Cristo"}

print(type(mi_diccionario))
print(mi_diccionario)

#como acceder 

print(mi_diccionario["edad"])

##################################

#alterar valores

mi_diccionario["nombre"] = "Lobotec"

print(mi_diccionario["nombre"])
print(mi_diccionario)
#agregar elementos

mi_diccionario["profesion"] = "lammer"

print(mi_diccionario)

#eliminar elementos
del mi_diccionario["ciudad"]

print(mi_diccionario)


#########################################

#comprobar que una clave esta en ese mi_diccionario

if "edad" in mi_diccionario:
    print("esta clave existe en el diccionario")
else:
    print("esta clave no existe en el diccionario")


#########################################################

#iterar en un diccionario

for key, value in mi_diccionario.items():
    print(f"para la clave {key} tenemos el valor: {value}")

#############################################################

print(f"la longitud del diccionario es de{len(mi_diccionario)} elementos")
##########################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#limpiar diccionario

#mi_diccionario.clear()
print(mi_diccionario)

###################################################################################
#Diccionarios de comprension

cuadrados = {x: x**2 for x in range(6)}

#print(cuadrados)
print(cuadrados.keys())
print(cuadrados.values())

###########################################

#get te permite buscar y si no lo encuentra pone lo que queres


print(mi_diccionario.get("nombre", "no encontrado"))

print(mi_diccionario.get("nombr", "no encontrado"))

mi_diccionario2 = {"ciudad": "MonteCristo", "mascota": "Tobi" }

mi_diccionario.update(mi_diccionario2)

print(mi_diccionario)
###################################################################
#Diccionarios anidados

my_dict = {
    "nombre": "Juan",
    "hobbies": {"primero": "musica", "segundo": "Futbol"},
    "edad": 24
        }
print(my_dict)

print(my_dict["hobbies"]["primero"])

########################################
#iterar

for element in my_dict.values():
    print(element)

for key, value in my_dict.items():
    print(f"[{key}]: {value}")


