
peso = int(input("Ingrese su peso en kilogramos"))
estatura = int(input("Ingrese su estatura en metros"))

imc = peso/(estatura ^ 2)

print("Tu indice de masa corporal es", round(imc, 2))
