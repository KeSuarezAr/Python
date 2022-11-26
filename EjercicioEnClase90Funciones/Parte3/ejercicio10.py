respuesta = input("Desea pizza vegetariana? ").lower()
contador = 0

ingredientesDefault = ["Mozzarella", "Tomate"]
ingredientesVegetarianos = ["Pimiento", "Tofu"]
ingredientesNoVegetarianos = ["Peperoni", "Jamon", "Salmon"]

ingredientesCliente = ingredientesDefault.copy()

if respuesta == "si":
    pizza = "Vegetariana"
    respuesta = input("Desea Pimiento ").lower()
    if respuesta == "si":
        ingredientesCliente.append(ingredientesVegetarianos[contador])

    else:
        contador += 1
        respuesta = input("Desea Tofu ").lower()
        if respuesta == "si":
            ingredientesCliente.append(ingredientesVegetarianos[contador])
else:
    pizza = "No Vegetariana"
    respuesta = input("Desea Peperoni ").lower()
    if respuesta == "si":
        ingredientesCliente.append(ingredientesNoVegetarianos[contador])
    else:
        contador += 1
        respuesta = input("Desea Jamon ").lower()
        if respuesta == "si":
            ingredientesCliente.append(ingredientesNoVegetarianos[contador])
        else:
            contador += 1
            respuesta = input("Desea Salmon ").lower()
            if respuesta == "si":
                ingredientesCliente.append(
                    ingredientesNoVegetarianos[contador])

print("Pizza", pizza, ingredientesCliente)
