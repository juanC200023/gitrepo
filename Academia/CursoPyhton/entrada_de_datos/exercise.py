while True:
    try:
        edad = int(input("\n[+] Dime tu edad: "))
        print(f"\n[+] Perfecto, deberias cumplir {edad+1}")
        break
    except ValueError:
        print(f"\nEl tipo de dato introducido es incorrecto")

