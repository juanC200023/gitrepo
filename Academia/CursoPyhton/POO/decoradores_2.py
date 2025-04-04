#!/usr/bin/env python3

import time

def cronometro(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        funcion()
        final = time.time()

        print(f"Tiempo total transcurrido en la funcion {funcion.__name__}: {final - inicio}")
        print(args)
    return envoltura

@cronometro
def pausa_corta(*args, **kwargs):
    time.sleep(1)
@cronometro
def Pausa_larga(*args, **kwargs):
    time.sleep(2)

pausa_corta(2, 3, 4, 6, 7, 8)
Pausa_larga()



