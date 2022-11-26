fecha = input("ingrese la fecha en el formato : ")

dia = fecha[:fecha.find("/")]
mesanio = fecha[fecha.find('/')+1:]
mes = mesanio[:mesanio.find('/')]
anio = fecha[fecha.find("/", 4)+1:]

print("dia: " + dia)
print("mes: " + mes)
print("anio: " + anio)
