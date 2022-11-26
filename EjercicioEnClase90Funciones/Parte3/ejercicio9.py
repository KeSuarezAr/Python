puntuacion = float(input("Ingrese su edad "))
seleccionado = False

if puntuacion < 4:
    print("El precio de entrada es gratis")

if puntuacion >= 4 and puntuacion < 18:
    print("El precio de entrada es 5$")
    
if puntuacion >= 18:
    print("El precio de entrada es 10$")
