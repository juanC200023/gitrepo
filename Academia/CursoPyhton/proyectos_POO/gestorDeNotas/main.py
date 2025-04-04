#!/usr/bin/env python3
import os
from gestor_notas import GestorNotas
def main():
    
    gestor = GestorNotas()

    while True:
        print(f"\n---------------\nMENU\n---------------")
        print("1. Agregar una nota")
        print("2. Leer todas las notas")
        print("3. Buscar por una nota")
        print("4. Eliminaruna nota")
        print("5. Salir")

        opcion = input("\n[+] Escoge una opcion: ")
        
        if opcion == "1":
            contenido = input("\n[+] Contenido de la nota: ")
            gestor.agregar_nota(contenido)

        elif opcion == "2":
            notas = gestor.leer_notas()

            print("\n[+] Mostrando todas las notas almacenadas:\n")

            for i, nota in enumerate(notas):
                print(f"{i}: {nota}")

        elif opcion == "3":
            texto_busqueda = input("\[+] Ingresa el texto a criterio a buscar en las notas: ")
            notas = gestor.buscar_nota(texto_busqueda)

            print(f"\n[+] Mostrando las notas que coinciden con el criterio de busqueda:\n")
            
            for i, nota in enumerate (notas):
                print(f"{i}: {nota}")

        elif opcion == "4":
            index = int(input(f"\n[+] Introduce el indice de la nota que quieres borrar: "))
            gestor.eliminar_nota(index)


        elif opcion == "5":
            break
        else:
            print("\n[!] La opcion indicada es incorrecta")

        input(f"\n[+] Presiona <enter> para continuar...")

        os.system('cls' if os.name == 'int' else 'clear')

if __name__ == '__main__':
    main()
