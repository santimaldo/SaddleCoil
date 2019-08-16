import numpy as np

class Radiofrecuencia(object):
    '''
    Esta clase contiene la información de la simulación realizada en COMSOL.
    
    Attributes
    ----------
    archivo : string
        Direccion del archivo que contiene la salida de la simulacion.
    
    parametros: array_like
        arreglo de parametros usados para la simulacion. COMPLETAR DOCUMENTACION.
    
    resultados : array_like
        resultados de la simulacion. COMPLETAR DOCUMENTACION.
        
    Methods
    -------
    set_parametros()
        Método utilizado para extraer los parámetros de la simulación del
        `archivo`, y los carga en el atributo `parametros`.    
    
    set_resultados()
        Método utilizado para extraer los resultados de la simulación del 
        `archivo`, y los carga en el atributo `resultados`.

    '''
    def __init__(self, Bx, By, Bz):
        
        
        self.Bx = Bx
        self.By = By
        self.Bz = Bz
        self.B1 = None # array_like. resultados de la simulacion
        self.B90 = None # 

	
    def set_parametros(self):
        #""" Método utilizado para extraer los parámetros de la simulación del 
        #`archivo`, y los carga en el atributo `parametros`. """
        # returns 
        pass
    
    def histograma(self):
        """
        Metodo que determina el Bxy con mayor cantidad de ocurrencias para ser
        usado como estimacion del tp. La salida es B90, el modulo del campo en
        xy con mayor cantidad de ocurrencias en el dominio.
        """
        # elijo 501 arbitrariamente. elijo impar porque vi que es mejor para
        # agarrar el cero.
        nbins = 501
        H, xedges, yedges = np.histogram2d(self.Bx, self.By, bins=nbins)
            
        indices = np.where(H == H.max())
        Bx90 = np.mean(xedges[indices[0][0]:indices[0][0]+2])
        By90 = np.mean(yedges[indices[1][0]:indices[1][0]+2])
    
        B90 = np.array([Bx90, By90])        
        B90 = np.linalg.norm(B90)
        self.B90 = B90
        return B90
    
    def generar_matriz_R(self, tp):
        """
        Metodo que genera la matriz de rotacion para aplicar el pulso. Esta 
        matriza es nx3x3, ya que es una matriz 3x3 para cada sitio.
        
        input
        -----
            tp : float
                tiempo de pulso. Se utiliza para determinar el angulo
                de rotacion.
        
        output
        ------
            R : array nx3x3
                Una matriz de rotacion para cada sitio. El uso de esta matriz
                es el producto con la magnetizacion via np.dot():
                    np.dot(R, M0)
                donde M0 es 3x1
        """
        # modulo del campo en el plano xy
        B1 = np.array([self.Bx, self.By])
        B1 = np.linalg.norm(B1, axis=0)

        # tres componentes de la direccion de rotacion. Cada U es un array de
        # n elementos, uno por cada sitio. Uz son ceros porque el campo en z
        # NO excita los spines.
        Ux = self.Bx/B1
        Uy = self.By/B1
        Uz = np.zeros_like(Ux)
        
        angulo = B1*tp
    
        # array de ceros y unos de tamano nx1
        zeros = np.zeros_like(Ux)
        ones = np.ones_like(Ux)
    
        # para definir la matriz uso la formula de Rodrigues:
        # https://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        