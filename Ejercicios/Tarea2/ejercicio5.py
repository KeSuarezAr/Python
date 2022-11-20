# Ejercicio 5:
# Define una función que si al darle una vocal mayúscula nos
# devuelva False, mientras que si es minúscula sea True.

def vocales():

    contador = 0
    vocal = input("Inserte su vocal: ")

    vocalesMinusculas = {

        0: "a",
        1: "e",
        2: "i",
        3: "o",
        4: "u"
    }

    vocalesMayusculas = {

        0: "A",
        1: "E",
        2: "I",
        3: "O",
        4: "U"
    }

    while contador != len(vocalesMayusculas):

        if vocal == vocalesMayusculas.get(contador):
            return False

        contador += 1

    contador = 0

    while contador != len(vocalesMinusculas):

        if vocal == vocalesMinusculas.get(contador):
            return True

        contador += 1

    return "No es una vocal"


print(vocales())
