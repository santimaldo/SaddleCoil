# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:02:40 2019

@author: santi
"""

import numpy as np
import matplotlib.pyplot as plt

d_E = 12e-3

path = 'S:/Doctorado/Dendritas/CellDesign/COMSOL/05/'
print('leyendo...')
archivo = 'datos_7mm.dat'
archivo = path + 'datos_4mm.dat'
archivo = './datos_test.dat'
archivo = './datos.dat'
resultados = np.loadtxt(archivo, comments='%', unpack=True)
# elimino los Nan
resultados = resultados.transpose()
resultados = resultados[~np.isnan(resultados).any(axis=1)]
resultados = resultados.transpose()
[X, Y, Bx, By, Bz, B1] = resultados
print('listo')


# plt.figure(1)
# plt.scatter(X, Y, c = Bz, cmap = 'RdBu')

# %%
nbins = 500

plt.figure(1)
ax1 = plt.subplot(311)
plt.hist(Bx, bins=nbins)

ax2 = plt.subplot(312, sharex=ax1, sharey=ax1)
plt.hist(By, bins=nbins)

ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
plt.hist(Bz, bins=nbins)

# %%
plt.figure(2)


#hx, xedge = np.histogram(Bx, bins=nbins)
#hy, yedge = np.histogram(By, bins=nbins)

H, xedges, yedges = np.histogram2d(Bx,By, bins=nbins)
BX, BY = np.meshgrid(xedges, yedges)
plt.pcolormesh(BX, BY, H)

# esxtraigo indices del maximo
ind = np.unravel_index(np.argmax(H, axis=None), H.shape)
Bx90 = np.mean(xedges[ind[0]:ind[0]+2])
By90 = np.mean(yedges[ind[1]:ind[1]+2])



# %%
plt.show()