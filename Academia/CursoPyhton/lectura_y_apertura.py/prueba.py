try:
    with open("prueba.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("\n[!] No ha sido posible encontrar este archivo")

