#!/usr/bin/env python3

#Los conjuntos no estan enumerados
#Los elementos deben ser unicos, por lo cual no pueden ser iguales

mi_conjunto = {1, 2, 3}

print(mi_conjunto)

#agregar elementos
mi_conjunto.add(4)

print(mi_conjunto)

#agregar mas conjuntos al conjuntos
mi_conjunto.update({5, 6})

print(mi_conjunto)
#Borrar

mi_conjunto.remove(3)
mi_conjunto.discard(7)#si el elemento no esta no va a hacer nada pero si esta lo borra
print(mi_conjunto)

########################################################################
#intersecciones: muestran los elementos del conjunto que se repiten en los dos
#ej:

mi_primer_conjunto = {1, 2, 3, 4, 5}
mi_segundo_conjunto = {3, 4, 5, 6}

conjunto_final = mi_primer_conjunto.intersection(mi_segundo_conjunto)

print(conjunto_final)

#########################################################################
#Uniones: quitan los elementos que se repiten

conjunto_final = mi_primer_conjunto.union(mi_segundo_conjunto)

print(conjunto_final)

###########################################################################
#verificar si un conjunto es subconjunto de otro

first_set = {1, 2, 3}
second_set = {1, 2, 3, 4, 5}

print(first_set.issubset(second_set))

######################################################################

mi_lista = [1, 5, 4, 4, 7, 5, 1, 12, 44, 12, 44]

no_repeat = list(set(mi_lista))
print(no_repeat)

####################################################################
#busquedas

my_set = set(range(10000))

print(1234 in my_set)

#################################################################3333
#ejemplo

users_facebook = {"Ana", "Savitar", "Juan", "Hackermate"}
users_X = {"Hackermate", "Juan", "Manolo", "Lucia"}


#Comprobar que usuarios estan en ambas plataformas

both_plataforms = users_facebook.intersection(users_X)

print(both_plataforms)

#Comprobar todos los usuarios que hay 

all_users_plataforms = users_X.union(users_facebook)

print(all_users_plataforms)

diferencias_entre_plataformas = users_facebook.difference(users_X)

print(diferencias_entre_plataformas)



