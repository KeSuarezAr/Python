renta = int(input("Cual es su renta anual "))
contador = 0
seleccionado = False

rentaimpositiva = [

    10000,
    20000,
    35000,
    60000,
    60000,

    5,
    15,
    20,
    30,
    45
]

while contador <= 4:
    if seleccionado != True:
        if renta < rentaimpositiva[contador]:
            print("Su renta impositiva es", rentaimpositiva[contador+5])
            seleccionado = True

        if renta > 60000:
            print("Su renta impositiva es", rentaimpositiva[contador])
            seleccionado = True

    contador += 1
