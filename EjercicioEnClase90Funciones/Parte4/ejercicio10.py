numero = int(input("Inserte un numero entero "))
contador = 2
while numero % contador != 0:
    contador += 1
if contador == numero:
    print(numero, "es primo")
else:
    print(numero, "no es primo")
