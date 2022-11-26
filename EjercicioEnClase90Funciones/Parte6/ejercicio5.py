def notas(valor):
    if valor < 5:
        return "Baja"
    elif valor < 7:
        return "Promedio"
    elif valor < 9:
        return "Buena"
    elif valor < 10:
        return "Muy Buena"
    else:
        return "Excelente"


def notasFinales(scores):
    return list(map(notas, scores))


print(notasFinales([7.3, 3, 4.6, 6.3, 9.2, 10, 9.2]))
