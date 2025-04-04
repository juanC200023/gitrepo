#!/usr/bin/env python3

juegos = ["Super Mario Bros", "Zelda: Breaht of the Wild", "Cyberpunk 2077", "Final Fantasy"]

tope = 500

#Generos
generos = {
    "Super Mario Bros": "Aventura",
    "Zelda: Breaht of the Wild": "Aventura",
    "Cyberpunk 2077": "Rol",
    "Final Fantasy": "Rol"
}

#Ventas y Stock
ventas_y_stock = {
    "Super Mario Bros": (400, 200),
    "Zelda: Breaht of the Wild": (600, 20),
    "Cyberpunk 2077": (60, 120),
    "Final Fantasy": (924, 3)
}
#clientes
clientes = {
    "Super Mario Bros": {"Marcelo", "Hackavis", "Securiters", "Lobotec"},
    "Zelda: Breaht of the Wild": {"Hackermate", "Hackavis", "Lucia", "Manolo", "Pepe"},
    "Cyberpunk 2077": {"Hackermate", "Pepe", "Raquel", "Albert"},
    "Final Fantasy": {"Lucia", "Manolo", "Pepe", "Securiters", "Patricia", "Moises"}
}

# mi_juego = "Super Mario Bros"

def sumario(juego):
    #Sumario

    print(f"\n[i] Resumen del juego {juego}\n")
    print(f"\t[+] Genero del juego: {generos[juego]}")
    print(f"\t[+] Total de ventas: {ventas_y_stock[juego][0]} unidades")
    print(f"\t[+] Total de stock: {ventas_y_stock[juego][1]} unidades")  
    print(f"\t[+] Clientes que han adquirido el juego: {', '.join(clientes[juego])}")

for juego in juegos:
    if ventas_y_stock[juego][0] > tope:
        sumario(juego)

#total de ventas de todos los juegos
ventas_totales = lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > tope)
print(f"\n[+] El total de ventas de todos los productos ha sido de: {ventas_totales()}")

