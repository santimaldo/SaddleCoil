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