"""
main.py
====================================
Módulo Principal del protyecto Saddle Coil
"""

from simulacion import *


archivo = './datos_test.dat'

sim = Simulacion(archivo)
[X, Y, Z, Bx, By, Bz] = sim.extraer_resultados()

