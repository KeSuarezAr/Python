# Ejercicio 7:
# Define una función que permita imprimir un mensaje en base a los valores
# tomados de una lista para comprobar si todos los de la lista son mayores o
# menores de edad.

def edad():

    listaValores = [15, 23, 32, 54, 15, 36, 17, 38,
                    59, 10, 31, 22, 33, 14, 16, 15,
                    16, 19, 18, 20, 20, 21, 12, 20]

    contador = 0

    while contador < len(listaValores):

        valor = listaValores[contador]
        if valor >= 18:
            print(listaValores[contador], ": Es Mayor de Edad")
        else:
            print(listaValores[contador], ": Es Menor de Edad")
        contador += 1


edad()
