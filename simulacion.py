import numpy as np


def extraer_resultados(archivo):
    # se usa asi:
    # [X, Y, Z, Bx, By, Bz] = self.extraer_resultados()
    
    resultados = np.loadtxt(archivo, comments='%', unpack=True)
    # elimino las filas que continenen NaN, para ello debo transponer.
    resultados = resultados.transpose()
    resultados = resultados[~np.isnan(resultados).any(axis=1)]                        
    
    #print("resultados '"+self.archivo+"' extraidos con exito.")

    #self.resultados = {'X': X, 'Y': Y, 'Z': Z,  'Bx': Bx, 'By': By, 'Bz': Bz}
    # el return esta transpuesto para poder usarlo asi: 
    # [X, Y, ...] = self.extraer_resultados()
    return resultados.transpose()


def nutacion(Bx,By):
    H, xedges, yedges = np.histogram2d(Bx,By, bins=500)
    
    indices = np.where(H == H.max())
    Bx90 = np.mean(xedges[indices[0][0]:indices[0][0]+2])
    By90 = np.mean(yedges[indices[1][0]:indices[1][0]+2])
    
    tp = np.pi / 2 / abs(Bx90 + 1j * By90)
    
    return tp

def Pulso90(M ,X, Y, Z, Bx, By, Bz, tp):