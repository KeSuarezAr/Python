frase = "Esta es una frase eseto es un ejemplo"


def grupoPalabras(frase):
    frase = frase.split()
    grupoPalabras = {}
    for i in frase:
        if i in grupoPalabras:
            grupoPalabras[i] += 1
        else:
            grupoPalabras[i] = 1
    return grupoPalabras


def palabrasRepetida(grupoPalabras):
    palabraMayor = ""
    frequenciaPalabra = 0
    for word, freq in grupoPalabras.items():
        if freq > frequenciaPalabra:
            palabraMayor = word
            frequenciaPalabra = freq
    return palabraMayor, frequenciaPalabra


print(grupoPalabras(frase))
print(palabrasRepetida(grupoPalabras(frase)))
