import math


def volumenesfera(radio):

    volumen = (4/3) * math.pi * radio**3

    return volumen


print("El volumen de la esfera es: ", volumenesfera(3))
