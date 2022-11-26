inversion = int(input("Ingrese su inversion anual "))
interes = int(input("Ingrese su interes anual "))
anios = int(input("Ingrese el numero de anios que desea invertir "))

total = anios * ((inversion * interes)/100)

print("Su capital obtenido total es", total)
