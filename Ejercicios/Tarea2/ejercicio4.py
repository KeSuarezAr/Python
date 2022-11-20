# Ejercicio 4:
# Define una función llamada num_min() que nos devuelva en pantalla el número
# menor entre 3 diferentes enteros. En caso de que todos sean iguales imprime en
# pantalla un mensaje indicándolo.

def num_min():
    digitos = 3
    numeros = []
    contador = 0

    while contador != digitos:
        contador += 1
        numeros.append(int(input("Ingrese un digito: ")))

    if numeros[0] == numeros[1] and numeros[1] == numeros[2]:
        print("Todos los numeros son iguales")
    else:
        numeros.sort()
        print(numeros[0])


num_min()
