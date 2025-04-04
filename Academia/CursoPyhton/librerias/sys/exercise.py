#!/usr/bin/env python3

import sys

print(f"\n[+] Nombre del script: {sys.argv[0]}")
print(f"\n[+] Mostrando todos los argumentos: {', '.join(argument for argument in sys.argv)}")

print(f"\n[+] Mostrando las rutas de python:\n")
for element in sys.path:
    print(element)

print(f"\n[+] Saliendo con un codigo 1 (no exitoso)")
sys.exit(1)
