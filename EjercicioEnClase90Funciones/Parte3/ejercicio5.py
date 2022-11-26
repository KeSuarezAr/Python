edad = int(input("Ingrese su edad: "))
ingresos = int(input("Ingrese sus ingresos: "))

if edad >= 18 and ingresos > 1000:
    print("Puede tributar")
else:
    print("No puede tributar")
