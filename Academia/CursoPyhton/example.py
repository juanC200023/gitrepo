#!/usr/bin/python3

port = 80

print(port)
print(type(port))

#inicializar una lista
my_ports = [22, 80, 443, 8080]

#agregar elementos a una lista
my_ports.append(4141)
my_ports.extend([85])
my_ports += [86, 87]

#Ordenar

my_ports = sorted(my_ports)

#Eliminar elementos

del my_ports[0]

#Recorrer una lista
for port in my_ports:
    print(f"Puerto: {port}")

print(f"La lista tiene un total de {len(my_ports)} elementos")
