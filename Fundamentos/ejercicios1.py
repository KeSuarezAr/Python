import random

# Declarar 2 variables que almacenen cada un numero, y compare si el primero es mayor al segundo, si el segundo es mayor al primero si ambos No es verdadero.\

numero1 = round(random.randrange(1, 50))
numero2 = round(random.randrange(1, 50))
numero3 = round(random.randrange(1, 50))

if numero1 > numero2 or numero2 > numero1 and numero3 > numero1:
    print("Es verdadero")
else:
    print("No es verdadero")

# Declare 3 edades. Compare
# 2.1 Si la primera edad es mayor que la segunda
# 2.2 Si la segunda edad es mayor que la primera
# 3.3 Si No es verdadero

edad1 = round(random.randrange(1, 80))
edad2 = round(random.randrange(1, 80))
edad3 = round(random.randrange(1, 80))

if edad1 > edad2 or edad2 > edad1 and edad3 > edad1:
    print("Es verdadero")
else:
    print("No es verdadero")

# Declare 3 notas. Compare
# 2.1 Si la primera nota es mayor que la segunda
# 2.2 Si la segunda nota es mayor que la primera
# 3.3 Si No es verdadero

nota1 = round(random.randrange(0, 10))
nota2 = round(random.randrange(0, 10))
nota3 = round(random.randrange(0, 10))

if nota1 > nota2 or nota2 > nota1 and nota3 > nota1:
    print("Es verdadero")
else:
    print("No es verdadero")
