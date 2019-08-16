"""
main.py
====================================
Módulo Principal del protyecto Saddle Coil
"""

import simulacion as sim
import matplotlib.pyplot as plt
import numpy as np

archivo = './datos_r15mm.dat'


[X, Y, Bx, By, Bz] = sim.extraer_resultados(archivo)

# Bx = np.ones(5456)
# By = np.zeros_like(Bx)


tp90 = sim.nutacion(Bx,By)

tp_nut = np.linspace(0, 6*tp90, 97)
i = 0
signal = []
phase = []
mz = []
for tp in tp_nut:
    # S: amplitud de la FID. Mz, magnetizacion que no fue excitada.
    M = sim.Pulso90(Bx, By, tp)
    S, Mz = sim.Medir(M)
    signal.append(S)
    #phase.append(fase)
    mz.append(Mz)
    print('Amplitud de la FID: ', S)
    print('Magnetizacion no excitada: ', Mz)
    print('fracción excitada: ', S/Mz*100, ' %')
    i += 1
    print('-------------------')
    
signal = np.array(signal)



# %%
t = tp_nut/tp90

plt.figure(11)
ax1 = plt.subplot(211)
plt.plot(t, signal, 'o-')

# ax2 = plt.subplot(312, sharex=ax1)
# phase = (phase + np.ones_like(phase) ) * 180/np.pi
# plt.plot(t, phase, 'o-')

ax3 = plt.subplot(212, sharex=ax1, sharey=ax1)
plt.plot(t, mz, 'o-')

"""
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
"""