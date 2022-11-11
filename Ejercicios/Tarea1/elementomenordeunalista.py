from random import random


def elementomenorlista():

    lista = []
    count = 0

    while count < 10:
        lista.append(round(random()*10))
        count += 1

    print(lista)
    return min(lista)


print("El numero mas pequenio es: ", elementomenorlista())
