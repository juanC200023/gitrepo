#!/usr/bin/env python3

ports_tcp = [21, 22, 25, 80, 8080, 445, 69]

#agregar puertos a la lista

ports_tcp.append(1337)


print(ports_tcp)

for port in ports_tcp:
    print(f"Este puerto es el {port}")
#borrar
cve_list = ['CVE-2023-1435', 'CVE-2022-3456', 'CVE-2023-0088']

cve_list.remove('CVE-2023-1435')
del cve_list[1]
print(cve_list)

#ordenar

ports_tcp.sort()
print(ports_tcp)

#invertir
atacks = ['phishing', 'DDoS', 'SQL Injection', 'Man In The Middle', 'Cross-Site Scripting']

print(atacks)

atacks.reverse()

print(atacks)

#crear sublistas

another_atacks_list = atacks[:3]

print(another_atacks_list)
#recorrer
i = 0 

while i < len(atacks):

    print(atacks[i])

    i += 1

for i, atack in enumerate(atacks):
    print(f"Para la posicion {i} tendriamos el ataque {atack}")

#creando una lista nueva atraves de otra
attacks_uppercase = [atack.upper() for atack in atacks]

print(attacks_uppercase)

#combinar listas

names = ['juan', 'savitar', 'hackermate', 'astralis']

edades = [23, 34, 13, 45]

for name, edad in zip(names, edades):
    print(f"Name {name} tiene {edad} years")


#Limpiar toda una lista

names.clear()

print(len(names))

#quitar el elemento y agregarlo en una variable

deleted_attack = attacks_uppercase.pop(2)

print(attacks_uppercase)

print(f"El ataque eliminado ha sido {deleted_attack}")

#agregar un elemento en una posicion dada sin eliminar el otro

edades.insert(2, 49)

print(edades)


