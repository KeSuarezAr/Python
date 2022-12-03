import math


class Punto:
    def __init__(self, coordenada_X=0, coordenada_Y=0):

        self.coordenada_X = coordenada_X
        self.coordenada_Y = coordenada_Y

    def cuadrante(self):
        if self.coordenada_X > 0 and self.coordenada_Y > 0:
            print("Se encuentre en el primer cuadrante")
        elif self.coordenada_X < 0 and self.coordenada_Y > 0:
            print("Se encuentre en el segundo cuadrante")
        elif self.coordenada_X < 0 and self.coordenada_Y < 0:
            print("Se encuentre en el tercer cuadrante")
        elif self.coordenada_X > 0 and self.coordenada_Y < 0:
            print("Se encuentre en el cuarto cuadrante")
        elif self.coordenada_X != 0 and self.coordenada_Y == 0:
            print("Se encuentra sobre el eje X")
        elif self.coordenada_X == 0 and self.coordenada_Y != 0:
            print("Se encuentra sobre el eje Y")
        elif self.coordenada_X == 0 and self.coordenada_Y == 0:
            print("Se encuentra sobre el origen")
        else:
            print("Se encuentra en algun otro punto")

    def vector(self, a):
        vectorX = a.coordenada_X - self.coordenada_X
        vectorY = a.coordenada_Y - self.coordenada_Y
        print("El vector es:", vectorX, ",", vectorY)

    def distancia(self, p):
        dist = math.sqrt((p.coordenada_X - self.coordenada_X)**2 +
                         (p.coordenada_Y - self.coordenada_Y)**2)
        print("La distancia entre los puntos es", dist)


A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)


class Rectangulo:
    def __init__(self, a, b):

        self.coordenadaInicial = a
        self.coordenadaFinal = b

    def mayor(self):

        if self.coordenadaInicial > self.coordenadaFinal:
            return True
        else:
            return False

    def base(self, base, c):

        if Rectangulo.mayor == False:

            self.base = c.coordenadaFinal
            print("la base del rectangulo es:", base)

    def altura(self, altura, d):

        if Rectangulo.mayor == True:

            self.altura = d.coordenadaInicial
            print("La altura del rectangulo es:", altura)

    def area(self,c,d):

        self.area = c.base * d.altura


A = Rectangulo(A, B)

A.base
A.altura
A.area
