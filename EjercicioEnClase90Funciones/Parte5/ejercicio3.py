def factorial(numero):
    tmp = 1
    for contador in range(numero):
        tmp *= contador+1
    return tmp


print("Su factorial es", factorial(int(input("Ingrese un numero "))))
