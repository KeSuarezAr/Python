# Ejercicio 8:
# Define una función que permita multiplicar los números de una lista y sumar
# sus resultados.

def multiplicar():

    listaMultiplicar = [15, 23, 32, 54, 15, 36, 17, 38,
                        59, 10, 31, 22, 33, 14, 16, 15,
                        16, 19, 18, 20, 20, 21, 12, 20]

    listaSuma = []
    listaFinal = []

    contador = 0

    while contador < len(listaMultiplicar):
        listaSuma.append(
            listaMultiplicar[contador] * listaMultiplicar[contador+1])
        contador += 2

    contador = 0

    while contador < len(listaSuma):
        listaFinal.append(
            listaSuma[contador] + listaSuma[contador+1])
        contador += 2

    print(listaFinal)


multiplicar()
