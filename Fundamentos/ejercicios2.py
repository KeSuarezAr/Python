# Calcular los primeros 50 numeros impares

def impar():

    i = 1
    lista = []

    while i <= 50:

        valor = i/2

        if ((valor).is_integer()) == False:

            lista.append(i)

        i += 1

    print(lista)


impar()

# Calcular los primeros 20 numeros pares, pero retirar el 10


def par():

    i = 1
    lista = []

    while i <= 50:

        valor = i/2

        if ((valor).is_integer()) == True:

            lista.append(i)

        i += 1

    lista.remove(10)
    print(lista)


par()


# Calcular los primeros 20 numeros pares, pero retirar el 10


def multiplos():

    i = 1
    lista = []

    while i <= 50 and len(lista) != 3:

        valor = i/5

        if ((valor).is_integer()) == True:

            lista.append(i)

        i += 1

    print(lista)


multiplos()
