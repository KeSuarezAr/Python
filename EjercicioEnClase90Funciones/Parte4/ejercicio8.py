contador = 0
contador1 = 1
numero = int(input("Ingrese un numero: "))
triangulo = []

while contador < numero:
    triangulo.reverse()
    triangulo.append(contador1)
    triangulo.reverse()
    x = "".join(str(triangulo))
    print(x)
    contador += 1
    contador1 += 2
