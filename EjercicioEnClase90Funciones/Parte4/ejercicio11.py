palabra = [*input("Ingrese una palabra: ")]
contador = 0
leng = len(palabra)

palabra.reverse()

while contador < leng:
    print(palabra[contador])
    contador += 1
