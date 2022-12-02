edadUsuario = int(input("Ingrese su edad: "))

if edadUsuario <= 17:
    print("El usuario es menor a 18")
elif edadUsuario >= 18 and edadUsuario <= 49:
    print("El usuario es mayor de edad")
elif edadUsuario >= 50 and edadUsuario <= 120:
    print("El usuario es de tercera edad")
else:
    print("No existe en este rango")
