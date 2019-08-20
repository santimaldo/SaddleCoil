"""
main.py
====================================
Módulo Principal del protyecto Saddle Coil
"""

from SaddleCoil import Simulacion
import matplotlib.pyplot as plt

print('======================================================================')
archivo = './datos_r15mm.dat'

# creo el objeto simulacion.
# Esto extrae los resultados del archivo, define los campos, y estima el tp
sim = Simulacion(archivo=archivo)

# aplico una nutacion para determinar el valor de tp. el mismo se guarda
# en dicho atributo
print('Aplicando nutacion...')
sim.sim_nutacion()
print('\t Listo! tp = ', sim.get_tp())

# aplico un pulso de duracion tp
print('Aplicando pulso...')
sim.pulso()
# adquiero la senal, y la magnetizacion residual en z
S = sim.adquirir_senal()
print('\tListo!\n\t\t Amplitod de senal = ', S)
print('\t\t fraccion excitada', sim.fraccion_excitada*100, ' %')


print('======================================================================')
#region = sim.region90(Bx,By,tp)
#
#print('Bx90:\n', Bx[region])
#
#print('Amplitud de la FID: ', S)
#print('Magnetizacion no excitada: ', Mz)
#print('fracción excitada: ', S/Mz*100, ' %')
#
#print('-------------------')
#
#Mx, My, Mz = M.transpose()
#
#plt.figure(1)
#nbins = 501
#ax1 = plt.subplot(311)
#plt.hist(Mx, bins=nbins)
#ax2 = plt.subplot(312, sharex=ax1, sharey=ax1)
#plt.hist(My, bins=nbins)
#ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
#plt.hist(Mz, bins=nbins)
#plt.show()
