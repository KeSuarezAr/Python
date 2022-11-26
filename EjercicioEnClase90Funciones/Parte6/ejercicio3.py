
def lista(funcion, lista):
    l = []
    for contador in lista:
        if funcion(contador):
            l.append(contador)
    return l


def par(numero):
    return numero % 2 == 0


print(lista(par, [5, 10, 15, 20, 25, 30]))
