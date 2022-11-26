nombreUsuario = input("Ingrese su nombre completo ")
contador = 0

while contador < 3:
    if contador == 0:
        print(nombreUsuario.lower())
        contador += 1

    if contador == 1:
        print(nombreUsuario.upper())
        contador += 1

    if contador == 2:
        print(nombreUsuario.capitalize())
        contador += 1
