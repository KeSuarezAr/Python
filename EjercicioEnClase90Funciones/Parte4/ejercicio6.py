contador = 0
numero = int(input("Ingrese un numero: "))
triangulo = []

while contador < numero:
    triangulo.append("*")
    x = "".join(triangulo)
    print(x)
    contador += 1
