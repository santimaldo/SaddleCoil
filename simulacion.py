import numpy as np


class Simulacion(object):
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
    def __init__(self, archivo):
        self.archivo = archivo # string
        self.parametros = None # array_like
        self.resultados = None # array:like
	
    def set_parametros(self):
        #""" Método utilizado para extraer los parámetros de la simulación del 
        #`archivo`, y los carga en el atributo `parametros`. """
        # returns 
        pass
    
    def extraer_resultados(self):
        #""" Método utilizado para extraer los resultados de la simulación del 
        #`archivo`, y los carga en el atributo `parametros`. """
        # se usa asi:
        # [X, Y, Z, Bx, By, Bz] = self.extraer_resultados()
        
        resultados = np.loadtxt(self.archivo, comments='%', unpack=True)
        # elimino las filas que continenen NaN, para ello debo transponer.
        resultados = resultados.transpose()
        resultados = resultados[~np.isnan(resultados).any(axis=1)]
                             
        
        print("resultados '"+self.archivo+"' extraidos con exito.")

        #self.resultados = {'X': X, 'Y': Y, 'Z': Z,  'Bx': Bx, 'By': By, 'Bz': Bz}
        self.resultados = resultados
        # el return esta transpuesto para poder usarlo asi: 
        # [X, Y, ...] = self.extraer_resultados()
        return resultados.transpose()
        