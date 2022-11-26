n = int(input("Ingrese un valor "))
m = int(input("Ingrese otro valor "))
r = 0
contador = 0
sumacontador = 0

resultado = n/m
c = round(resultado)

while sumacontador < n:
    sumacontador += m
    r += 1

print(resultado)
print("El cociente es",c)
print("El resto es",r)
