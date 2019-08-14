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

def Pulso90(Bx, By, Bz, tp):
    B1 = np.array([Bx, By, Bz])
    B1 = np.linalg.norm(B1, axis=0)
    
    Ux = Bx/B1
    Uy = By/B1
    Uz = Bz/B1

    R = generar_matriz_R(Ux, Uy, Uz, tp)
    M0 = np.array([0,0,1])
    
    M = np.dot(R,M0)
    return M

def generar_matriz_R(Ux, Uy, Uz, tp):
    O = np.zeros_like(Ux)
    I = np.ones_like(Ux)
    
    
    

    
def Rot_y(vector,angulo):
    # definir matriz de rotacion
    c = np.cos(angulo)
    print('shape cos(angulo): ', c.shape)
    s = np.sin(angulo)
    O = np.zeros_like(angulo)
    I = np.ones_like(angulo)
    Ry = np.array([[c, O, s], [O, I, O], [-s, O, c]])
    print('shape Ry: ', Ry.shape)
    Ry = np.rollaxis(Ry,-1)
    print('shape Ry: ', Ry.shape)
    #rint('Ry: ', Ry)
    return np.dot(Ry, vector)


def Rot_y(vector,angulo):
    # definir matriz de rotacion
    c = np.cos(angulo)
    print('shape cos(angulo): ', c.shape)
    s = np.sin(angulo)
    O = np.zeros_like(angulo)
    I = np.ones_like(angulo)
    Ry = np.array([[c, O, s], [O, I, O], [-s, O, c]])
    
    print('shape Ry: ', Ry.shape)
    Ry = np.rollaxis(Ry,-1)
    print('shape Ry: ', Ry.shape)
    #rint('Ry: ', Ry)
    return np.dot(Ry, vector)


def Rot(kx, ky, kz, angulo):
    #kx = direccion[:,0]
    #ky = direccion[:,1]
    #kz = direccion[:,2]
    print('rotacion...')
    print(kx, ky, kz)
    zeros = np.zeros_like(kx)
    ones = np.ones_like(kx)
    
    K = np.array([[zeros, -kz, ky], [kz, zeros, -kx], [-ky, kx, zeros]])
    K = np.rollaxis(K, -1)
    I = np.array([[ones, zeros, zeros], [zeros, ones, zeros], [zeros, zeros, ones]])
    I = np.rollaxis(I, -1)
    print('I:', I, I.shape)
    
    R = I + np.sin(angulo) * K + (1-np.cos(angulo)) * K**2
    

    M0 = np.array([0,0,1])
    return np.dot(R, M0)