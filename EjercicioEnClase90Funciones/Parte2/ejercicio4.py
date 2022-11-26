
x = [*input("Inserte su numero incluyendo la extension: ")]


contador1 = x.index("-")

del x[:contador1+1]

contador1 = x.index("-")

del x[contador1:]

print(x)
