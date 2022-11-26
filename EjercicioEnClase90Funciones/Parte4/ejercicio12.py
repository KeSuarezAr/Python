contador = 0
numerovocales = 0

palabra = [*input("Inserte su palabra: ")]
letra = input("Ingrese su letra ")


while contador < (len(palabra)):

    if palabra[contador] == letra:

        numerovocales += 1

    contador += 1


print("El numero de vocales es: ", numerovocales)
