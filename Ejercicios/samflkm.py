def vocales():

    count1 = 0
    count2 = 0

    numerovocales = 0

    vocales = {

        0: "a",
        1: "e",
        2: "i",
        3: "o",
        4: "u"
    }

    palabra = [*input("Inserte su palabra: ")]

    while count1 < len(palabra):

        while count2 < (len(palabra)+1):

            # print(palabra[count1])
            # print(vocales.get(count2))

            if palabra[count1] == vocales.get(count2):

                numerovocales += 1

            count2 += 1

        count1 += 1
        count2 = 0

    print(numerovocales)


vocales()
