n = int(input("Ingrese un numero entero positivo "))
contador = 1
lista = []
listasuma = []

while contador <= n:

    lista.append(contador)
    contador += 1

print(lista)
contador = 0

if (len(lista)/2) == 0:

    while contador < n:
        listasuma.append(
            lista[contador] + lista[contador+1])
        contador += 2

    print(listasuma)

else:
    print("Hay un numero flojo")
