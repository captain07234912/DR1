
from LibreriaGL import *
import numpy as np

"""
Universidad del Valle de Guatemala
Graficas por computadora
Render
Jorge Suchite Carnet 15293
07/09/2020
DR1 :  Spheres and Materials

"""

White = (1,1,1)
class Material (object):
    def __init__(self, diffuse = White):

        self.diffuse = diffuse

        return

class Intersect (object):
    def __init__(self,distance):
        self.distance = distance
class Sphere(object):
    def __init__(self, center, radius, material ):
        self.center = center
        self.radius = radius
        self.material = material


    def ray_intersect(self, orig, dir ):
        L = magnum(self.center, orig)
        tca = productopunto(L, dir)
        l = magnum2(L)  # magnitud de L
        d = (l ** 2 - tca ** 2) ** 0.5
        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1

        if t0 < 0:  # t0 ahora es t1
            return None



        return  Intersect(distance= t0)