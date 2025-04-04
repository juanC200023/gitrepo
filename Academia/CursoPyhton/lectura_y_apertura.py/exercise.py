#example.txt ("Hola mundo!")
# f = open("example.txt", "w")
#f.write("Hola mundo!")

#with open("example.txt", "w") as f:
 #   f.write("hola mundo")

with open("/etc/hosts", "r") as f:
    #    file_content = f.read()
    for line in f:
        print(line.strip()) #.strip para quitar el salto de linea
#first_linea = f.readline()
#print(first_linea) es para ver el contenido de la primera linea

mi_lista = ["primera linea\n", "segunda linea\n", "tercera linea\n", "cuarta linea"]

with open("example2.txt", "w") as k:
    k.writelines(mi_lista)

###################################################
with open("prueba.txt", "w") as j:
    print("Hola mundo", file=j)
