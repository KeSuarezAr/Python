def cuadrado(numeros):

    lista = []
    for contador in numeros:
        lista.append(contador**2)
    return lista


def calculos(numeros):

    calculo = {}
    calculo["media"] = sum(numeros)/len(numeros)
    calculo["varianza"] = sum(cuadrado(numeros)) / \
        len(numeros)-calculo["media"]**2
    calculo["desviacion tipica"] = calculo["varianza"]**0.5
    return calculo


print(calculos([20, 40, 60, 80, 100]))
