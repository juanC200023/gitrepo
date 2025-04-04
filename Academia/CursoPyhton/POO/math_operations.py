def suma(x, y):

    return x + y
def resta(x, y):

    return x - y

def multiplicacion(x, y):

    return x * y

def division(x, y):

    if y == 0:
        raise ValueError("[!]Error de valor. No se puede dividir un numero por cero")
    else:
        return x / y

