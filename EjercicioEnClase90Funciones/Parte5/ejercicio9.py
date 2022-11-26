def maximocomundivisor(numero1, numero2):
    menor = 0
    while (numero2 > 0):
        menor = numero2
        numero2 = numero1 % numero2
        numero1 = menor
    return numero1


def minimocomunmultiplo(numero1, numero2):

    if numero1 > numero2:
        mayorque = numero1
    else:
        mayorque = numero2
    while (mayorque % numero1 != 0) or (mayorque % numero2 != 0):
        mayorque += 1
    return mayorque


print(maximocomundivisor(20, 30))
print(minimocomunmultiplo(20, 30))
