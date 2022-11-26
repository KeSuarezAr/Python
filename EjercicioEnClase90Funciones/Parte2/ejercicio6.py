
count1 = 0
count2 = 0

vocales = {

    0: "a",
    1: "e",
    2: "i",
    3: "o",
    4: "u"
}

frase = [*input("Ingrese una frase ").lower()]

while count1 < len(frase):

    while count2 < (len(frase)+1):

        # print(frase[count1])
        # print(vocales.get(count2))

        if frase[count1] == vocales.get(count2):

            frase[count1] = frase[count1].capitalize()

        count2 += 1

    count1 += 1
    count2 = 0


x = "".join(frase)

print(frase)
print(x)
