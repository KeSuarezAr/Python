def paroimpoar():

    numero = int(input("Inserte un numero para verificar si es par: "))

    valor = numero/2

    if ((valor).is_integer()) == True:
        print("El numero es par")
    else:
        print("El numero es inpar")


paroimpoar()
