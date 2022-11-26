cantidad = int(input("Ingrese la cantidad en la cuenta de ahorro "))
interes = 4
porcentaje = ((cantidad * interes)/100)

print("El interes del primer año es", round(porcentaje*1, 2))
print("El interes del segundo año es", round(porcentaje*2, 2))
print("El interes del tercer año es", round(porcentaje*3, 2))
