def decimal(numero):
    numero = list(numero)
    numero.reverse()
    decimal = 0
    for contador in range(len(numero)):
        decimal += int(numero[contador]) * 2 ** contador
    return decimal


def binario(numero):
    binarios = []
    while numero > 0:
        binarios.append(str(numero % 2))
        numero //= 2
    binarios.reverse()
    return "".join(binarios)


print(decimal("11111111"))
print(binario(255))
