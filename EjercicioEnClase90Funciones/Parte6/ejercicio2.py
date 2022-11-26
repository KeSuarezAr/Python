def descuento(precio, descuento):
    return precio - precio * descuento / 100


def descuento2(precio, descuento2):
    return precio + precio * descuento2 / 100


def cesta(cesta, funcion):
    total = 0
    for precio, descuento in cesta.items():
        total += funcion(precio, descuento)
    return total


print('El precio es:', cesta({500: 50, 500: 50, 500: 50}, descuento2))
