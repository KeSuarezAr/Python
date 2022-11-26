def descuento(precio, descuento):
    return precio - precio * descuento / 100


def iva(precio, porcentage):
    return precio - precio * descuento / 100


def cesta(cesta, calculo):
    total = 0
    for precio, descuento in cesta.items():
        total += calculo(precio, descuento)
    return total


descuento(500, 50)

iva(500, 25)

cesta(500, 5)
