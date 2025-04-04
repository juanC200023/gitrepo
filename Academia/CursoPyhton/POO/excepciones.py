#!/usr/bin/env python3

try:
   num = "hola"/0 
except ZeroDivisionError:

    print("No se puede dividir un numero entre 0")

except TypeError:

    print("las operatorias solo se pueden realizar entre numeros")

else:

    print(f"La division de ambos numeros da como resultado{num}")


finally:

    print("Esto siempre se va a ejecutar")


x = -5 

if x < 0:
    raise Exception("No se pueden utilizar numeros negativos")
