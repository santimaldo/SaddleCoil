"""
main.py
====================================
Módulo Principal del protyecto Saddle Coil
"""

import simulacion as sim


archivo = './datos_test.dat'


[X, Y, Bx, By, Bz, B1] = sim.extraer_resultados(archivo)
