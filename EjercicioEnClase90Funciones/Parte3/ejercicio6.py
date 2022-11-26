nombre = [*input("Ingrese una nombre ").lower()]
genero = (input("Ingrese su genero: "))

contador = 0
grupo = False

letras = {

    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: "m",
    13: "n",
    14: "o",
    15: "p",
    16: "q",
    17: "r",
    18: "s",
    19: "t",
    20: "u",
    21: "v",
    22: "w",
    23: "x",
    24: "y",
    25: "z",
}


while contador <= 11:

    if nombre[0] == letras.get(contador) and genero == "Femenino":

        print("Pertenese al grupo A")
        grupo = True

    contador += 1

contador = 12

while contador <= 25:

    if nombre[0] == letras.get(contador) and genero == "Masculino":

        print("Pertenese al grupo A")
        grupo = True

    contador += 1

if grupo != True:
    print("Pertenece al grupo B")
