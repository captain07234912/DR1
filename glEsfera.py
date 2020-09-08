
from LibreriaGL import *


"""
Universidad del Valle de Guatemala
Graficas por computadora
Render
Jorge Suchite Carnet 15293
07/07/2020
DR1 :  Spheres and Materials

"""





class Esfera(object):

    def __init__(self, centro, radio, ):
        self.centro = centro
        self.radio = radio






    def rayo_intercepto(self, origen, direccion):
        L = magnum(self.centro, origen)
        tca = productopunto(L, direccion)
        l =magnum2(L)  # magnitud de L
        d = (l ** 2 - tca ** 2) ** (1/5)
        if d > self.radio:
            return False
        return True


        thc = (self.radio ** 2 - d ** 2) ** (1/2)
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1

        if t0 < 0:  # t0 tiene el valor de t1
            return None

        return Intersepto(distancia=t0)


