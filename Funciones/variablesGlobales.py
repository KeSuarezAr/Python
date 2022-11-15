salario = int(input("Ingrese su salario: "))


def calcularSalario(int: salario):

    global salario
    # salario = 300
    seguro = 50
    salarioTotal = salario - seguro
    return salarioTotal


print(type(salario))
print(calcularSalario(salario))
