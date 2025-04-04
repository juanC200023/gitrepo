#copiar imagen para meterla en un archivo

with open("/home/juanc/Desktop/juancruz/Fondos/fondo.png", "rb") as f_in, open("image.png", "wb") as f_out:
    file_content = f_in.read()
    f_out.write(file_content)
