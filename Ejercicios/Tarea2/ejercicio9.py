# Ejercicio 9:
# Crea un código que solicite ingresar el nombre de un archivo con su extensión y
# devuelva la extensión de la misma. Por ejemplo: La extensión de programando-
# aprenderpython.py es “.py”.

def extencion():

    archivo = [*input("Inserte su archivo incluyendo la extension: ")]

    contador1 = len(archivo) - (len(archivo) - archivo.index("."))

    del archivo[:contador1]

    print(archivo)


extencion()


def nombre():

    archivo = [*input("Inserte su archivo incluyendo la extension: ")]

    contador2 = archivo.index(".") - len(archivo)

    del archivo[contador2:]

    print(archivo)


nombre()
