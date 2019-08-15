import numpy as np
import matplotlib.pyplot as plt
from simulacion import *

# kx = np.array([0, 0, 1, -1])
# ky = np.array([0, 1, 0, 0])
# kz = np.array([1, 0, 0, 0])
#angulo = np.pi/2
kx = np.zeros(4)
ky = np.ones(4)
kz = np.zeros(4)
angulo = np.array([0.25, 0.5, 1, 1]) * np.pi

M, I, K, KxK,  R = Rot(kx,ky,kz, angulo)

# para visualizar mas facil:
M[np.abs(M)<1e-10] = 0
print('vector rotado: \n', M)

print('-----------------------------------')

# ahora pruebo las funciones posta
# supongamos un campo en x. COnsideremos 10 sitios, en todos el cualquiera, por ejemplo, 273
sitios = 10
campo = 273.0
Bx = np.ones(sitios) * campo
By = np.zeros(sitios)
Bz = np.zeros(sitios)

# hago una nutacion
#tp = nutacion(Bx,By)
tp, B90, Bx90, By90, Bz90 = nutacion(Bx, By, Bz)

#aplico Pulso
M = Pulso90(Bx, By, Bz, tp)

# para visualizar mas facil:
M[np.abs(M)<1e-10] = 0
