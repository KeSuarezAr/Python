def palabra(frase):

    words = frase.split()
    longitud = map(len, words)
    return dict(zip(words, longitud))


print(palabra("Esta es una frase"))
