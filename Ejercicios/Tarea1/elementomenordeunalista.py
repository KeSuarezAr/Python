from random import random


def elementomenorlista():

    lista = []
    x = 0

    while x < 10:
        lista.append(round(random()*10))
        x += 1

    print(lista)
    return min(lista)


print("El numero mas pequenio es: ", elementomenorlista())
