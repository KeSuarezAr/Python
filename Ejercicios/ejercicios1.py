from random import random
import math


def multiplicarsinsimbolo(ma, mb):

    x = 0
    mr = 0

    while x < mb:
        mr = mr + ma
        x += 1

    return mr


print(multiplicarsinsimbolo(2, 5))


def retornarnombrereves(nombre, apellido):

    nombreapellido = [nombre, apellido]
    nombreapellido.reverse()
    return nombreapellido


print(retornarnombrereves("Kevin", "Suarez"))


def elementomenorlista():

    lista = []
    x = 0

    while x < 10:
        lista.append(round(random()*10))
        x += 1

    print(lista)
    return min(lista)


print("El numero mas pequenio es: ", elementomenorlista())


def volumenesfera(radio):

    volumen = (4/3) * math.pi * radio**3

    return volumen


print("El volumen de la esfera es: ", volumenesfera(3))


def mayordeedad():

    edad = int(input("Inserte su edad: "))

    if edad >= 18:
        print("El usuario es mayor de edad")
    else:
        print("El usuario no es mayor de edad")


mayordeedad()


def paroimpoar():

    numero = int(input("Inserte un numero para verificar si es par: "))

    valor = numero/2

    if ((valor).is_integer()) == True:
        print("El numero es par")
    else:
        print("El numero es inpar")


paroimpoar()


def vocales():

    count1 = 0
    count2 = 0

    numerovocales = 0

    vocales = {

        0: "a",
        1: "e",
        2: "i",
        3: "o",
        4: "u"
    }

    palabra = [*input("Inserte su palabra: ")]

    while count1 < len(palabra):

        while count2 < (len(palabra)+1):

            # print(palabra[count1])
            # print(vocales.get(count2))

            if palabra[count1] == vocales.get(count2):

                numerovocales += 1

            count2 += 1

        count1 += 1
        count2 = 0

    print("El numero de vocales es: ", numerovocales)


vocales()
