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

def nutacion(Bx,By,Bz):
    nbins = 501
    campo = np.array([Bx,By,Bz]).T
    H, edges = np.histogramdd(campo, bins=nbins)
    xedges, yedges, zedges = edges

    print(xedges.shape, yedges.shape, zedges.shape)
    indices = np.where(H == H.max())
    Bx90 = np.mean(xedges[indices[0][0]:indices[0][0]+2])
    By90 = np.mean(yedges[indices[1][0]:indices[1][0]+2])
    Bz90 = np.mean(yedges[indices[2][0]:indices[2][0]+2])

    B90 = np.array([Bx90, By90, Bz90])
    B90[B90<np.max(B90)*1e-7] = 0
    print(B90)
    B90 = np.linalg.norm(B90)

    tp = np.pi / 2 / B90
    print(B90)
    return tp
    #return tp, B90, Bx90, By90, Bz90

def Pulso90(Bx, By, Bz, tp):
    B1 = np.array([Bx, By, Bz])
    B1 = np.linalg.norm(B1, axis=0)

    Ux = Bx/B1
    Uy = By/B1
    Uz = Bz/B1

    angulo = B1*tp
    print("angulo: ", angulo)
    R = generar_matriz_R(Ux, Uy, Uz, angulo)
    M0 = np.array([0,0,1])

    M = np.dot(R,M0)
    return M

def generar_matriz_R(Ux, Uy, Uz, angulo):
    zeros = np.zeros_like(Ux)
    ones = np.ones_like(Ux)

    U_matrix = np.array([[ zeros, -Uz   ,  Uy   ],
                         [ Uz   ,  zeros, -Ux   ],
                         [-Uy   ,  Ux   ,  zeros]]
                        )

    Uxy, Uxz, Uyz = [Ux*Uy, Ux*Uz, Uy*Uz]
    U2_matrix = np.array([[Ux*Ux, Uxy  , Uxz  ],
                          [Uxy  , Uy*Uy, Uyz  ],
                          [Uxz  , Uyz  , Uz*Uz]]
                         )

    I = np.array([[ones, zeros, zeros], [zeros, ones, zeros], [zeros, zeros, ones]])

    R = np.cos(angulo) * I + np.sin(angulo) * U_matrix + (1-np.cos(angulo)) * U2_matrix
    # convierto en array nx3x3
    R = np.moveaxis(R,2,0)
    return R



#---------------------FUNCIONES DE PRUEBA
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
    """
    NO LOGRE HACER QUE FUNCIONE LA FORMULA DE RODRIGUES, TENDRE QUE HARDCODEAR
    """
    print('rotacion...')
    print(kx, ky, kz)
    zeros = np.zeros_like(kx)
    ones = np.ones_like(kx)

    K = np.array([[zeros, -kz   ,  ky   ],
                  [kz   ,  zeros, -kx  ],
                  [-ky  ,  kx   ,  zeros]]
                 )
    #K = np.moveaxis(K, 2, 0)

    kxy, kxz, kyz = [kx*ky, kx*kz, ky*kz]
    KxK = np.array([[kx*kx, kxy  , kxz  ],
                    [kxy  , ky*ky, kyz  ],
                    [kxz  , kyz  , kz*kz]])
    #KxK = np.moveaxis(KxK, 2, 0)
    I = np.array([[ones, zeros, zeros], [zeros, ones, zeros], [zeros, zeros, ones]])
    #I = np.moveaxis(I, 2, 0)
    #print('I:', I, I.shape)

    cos = np.cos(angulo)
    sin = np.sin(angulo)

    R = cos * I + sin * K + (1-cos) * KxK
    R = np.moveaxis(R,2,0)
    M0 = np.array([0,0,1])
    M = np.dot(R, M0)
    return M, I, K, KxK, R



def nutacion2D(Bx,By):
    H, xedges, yedges = np.histogram2d(Bx,By, bins=2001)

    indices = np.where(H == H.max())
    Bx90 = np.mean(xedges[indices[0][0]:indices[0][0]+2])
    By90 = np.mean(yedges[indices[1][0]:indices[1][0]+2])

    B90 = np.array([Bx90, By90])
    print(B90)
    B90 = np.linalg.norm(B90)

    tp = np.pi / 2 / B90

    print(B90)

    return tp
