puntuacion = float(input("Cual es calificacion "))

if puntuacion < 0.4:
    print("Su nivel de satisfaccion es inaceptable")

if puntuacion >= 0.4 and puntuacion < 0.6:
    print("Su nivel de satisfaccion es aceptable")

if puntuacion >= 0.6:
    print("Su nivel de satisfaccion es meritorio")
