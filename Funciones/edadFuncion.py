def edadCalcular(edad, nombre):

    nombre = input("Ingrese su nombre: ")
    edad = int(input("Porfavor ingrese su edad: "))
    if edad >= 18 and edad <= 65:
        print("Es mayor de edad")
    elif edad >= 65:
        print("Es tercera edad")
    else:
        print("Es menor de edad")


edadCalcular(1, "me")
