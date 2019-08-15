"""
main.py
====================================
Módulo Principal del protyecto Saddle Coil
"""

import simulacion as sim
import matplotlib.pyplot as plt


archivo = './datos.dat'


[X, Y, Bx, By, Bz, B1] = sim.extraer_resultados(archivo)

tp = sim.nutacion(Bx,By,Bz)

M = sim.Pulso90(Bx, By, Bz, tp)

# S: amplitud de la FID. Mz, magnetizacion que no fue excitada.
S, Mz = sim.Medir(M)

print('Amplitud de la FID: ', S)
print('Magnetizacion no excitada: ', Mz)
print('fracción excitada: ', S/Mz*100, ' %')

print('-------------------')

Mx, My, Mz = M.transpose()

plt.figure(1)
nbins = 'auto'
ax1 = plt.subplot(311)
plt.hist(Mx, bins=nbins)
ax2 = plt.subplot(312, sharex=ax1, sharey=ax1)
plt.hist(My, bins=nbins)
ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
plt.hist(Mz, bins=nbins)
plt.show()
