import os

ruta = os.path.join("mi_directorio", "mi_archivo.txt")

print(f"\n[+] Ruta: {ruta}")

archivo = os.path.basename(ruta)

print(f"\n[+] Nombre del archivo: {archivo}")

directorio = os.path.dirname(ruta)

print(f"\n[+] Nombre del directorio donde esta el archivo: {directorio}")
