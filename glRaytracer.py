from LibreriaGL import *
from ModelObj import *
from glEsfera import *
from Render import Render
import random

"""
Universidad del Valle de Guatemala
Graficas por computadora
Raytracing
Jorge Suchite Carnet 15293
07/09/2020

DR1 Spheraes and materials

"""

width = 500
height = 300



sape = Render(width,height)
ss = Esfera((-2,1,-10),1.5)
sape.rtxrender(ss)


sape.glFinish('output.bmp')

