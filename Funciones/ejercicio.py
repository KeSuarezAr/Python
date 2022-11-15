import random


def calificarNota(nota):
    print("Su calificacion es: ", nota)
    if nota <= 10 and nota >= 9:
        print("Excelente.")
    elif nota < 9 and nota >= 8:
        print("Muy Bueno")
    elif nota < 8 and nota >= 7:
        print("Bueno")
    else:
        print("Reprobado")


calificarNota(random.randint(0, 10))
