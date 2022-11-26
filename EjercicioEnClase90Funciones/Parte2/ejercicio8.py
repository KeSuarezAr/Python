valor = input("ingrese un precio en dolares con dos decimales: ")

precio = valor[:(valor.index("."))] + ""
centavos = "" + valor[(valor.index(".")+1):]

print(precio, "dolares")
print(centavos, "centavos")
