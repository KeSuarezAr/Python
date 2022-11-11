def multiplicarsinsimultiplicadorolo(numeroBase, multiplicador):

    count = 0
    resultado = 0

    while count < multiplicador:
        resultado = resultado + numeroBase
        count += 1

    return resultado


print(multiplicarsinsimultiplicadorolo(2, 5))
