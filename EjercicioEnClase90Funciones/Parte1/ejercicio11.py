numeroNoDelDia = int(
    input("Ingrese el número de barras vendidas que no son del día "))

coste = 3.49
porcentaje = 60
descuento = round((coste*porcentaje)/100, 2)
preciototal = round((coste - descuento)*numeroNoDelDia, 2)

print("El precio habitual es", coste, "El descuento es",
      descuento, "Y el precio final es", preciototal)
