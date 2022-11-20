# Ejercicio 2:
# Define una función llamada num_max() que nos devuelva en pantalla el número
# mayor entre 4 diferentes enteros. No definas ningún valor a imprimir en caso
# de que ambos números sean iguales.

def num_max():
    digitos = 4
    numeros = []
    contador = 0

    while contador != digitos:
        contador += 1
        numeros.append(int(input("Ingrese un digito: ")))

    numeros.sort(reverse=True)
    print(numeros[0])


num_max()
