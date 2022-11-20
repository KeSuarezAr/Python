# Ejercicio 1:
# • Define una función llamada menorque() que nos devuelva en pantalla el número
# menor entre dos enteros.

def menorque():
    digitos = int(input("Ingrese cuantos digitos desea ingresar: "))
    numeros = []
    contador = 0

    while contador != digitos:
        contador += 1
        numeros.append(int(input("Ingrese un digito: ")))

    numeros.sort()
    print(numeros[0])


menorque()
