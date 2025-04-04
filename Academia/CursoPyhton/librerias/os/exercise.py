#!/usr/bin/env python3

import os

directorio_actual = os.getcwd()

print(f"\n[+] Directorio actual de trabajo: {directorio_actual}")

files = os.listdir(directorio_actual) #Lista los directorios

print(f"\n[+] Listando los archivos existentes en el directorio: {directorio_actual}\n")

for file in files:
    print(file)

if not os.path.exists('mi_directorio'): 
    os.mkdir("mi_directorio")

    print(f"\n[+] Directorio 'mi_directorio' creado:\n")
    files = os.listdir(directorio_actual)
    for file in files:
        print(file)

print(f"\n[+] Existe el archivo 'mi_archivo.txt' -> {os.path.exists('mi_archivo.txt')}")

value = get_env = os.getenv('SUDO_COMMAND')
print(f"\n[+] Valor de la variable de entorno 'SUDO_COMMAND': {value}")
