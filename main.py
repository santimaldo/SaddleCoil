"""
main.py
====================================
Módulo Principal del protyecto Saddle Coil
"""

import simulacion as sim
import matplotlib.pyplot as plt


archivo = './datos_r15mm.dat'


[X, Y, Bx, By, Bz] = sim.extraer_resultados(archivo)

tp = sim.nutacion(Bx,By)

M = sim.Pulso90(Bx, By, 0.4*tp)

# S: amplitud de la FID. Mz, magnetizacion que no fue excitada.
S, Mz = sim.Medir(M)

region = sim.region90(Bx,By,tp)

print('Bx90:\n', Bx[region])

print('Amplitud de la FID: ', S)
print('Magnetizacion no excitada: ', Mz)
print('fraccion excitada: ', S/Mz*100, ' %')

print('-------------------')

Mx, My, Mz = M.transpose()

plt.figure(1)
nbins = 501
ax1 = plt.subplot(311)
plt.hist(Mx, bins=nbins)
ax2 = plt.subplot(312, sharex=ax1, sharey=ax1)
plt.hist(My, bins=nbins)
ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
plt.hist(Mz, bins=nbins)
plt.show()
