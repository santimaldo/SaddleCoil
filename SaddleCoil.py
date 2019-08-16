# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:11:20 2019

@author: santi
"""

import numpy as np
# mis modulos:
from radiofrecuencia import Radiofrecuencia
from magnetizacion import Magnetizacion


class Simulacion:
    """
    Esta clase contiene la información de la simulacion realizada en COMSOL.
    Ademas, los metodos para realizar el analisis
    
    Attributes
    ----------
    archivo : string
        direccion y nombre del archivo exportado de COMSOL
    
    b1 : objeto de clase Radiofrecuencia
        Campos generados por la simulacion en COMSOL
    
    magnetizacion: objeto de clase Magnetizacion
        Contiene la magnetizacio, la cual se modifica mediante pulsos. Su valor
        inicial es el equilibrio, es decir, vectores unidad en direccion z.
    
    tp : float
        tiempo de pulso.
        
    Methods
    -------
    set_parametros()
        Método utilizado para extraer los parámetros de la simulación del
        `archivo`, y los carga en el atributo `parametros`.    
    
    set_resultados()
        Método utilizado para extraer los resultados de la simulación del 
        `archivo`, y los carga en el atributo `resultados`.
    """

    
    
    def __init__(self, archivo=None, b1=None, magnetizacion=None, tp=None):
        
        self.b1 = b1
        self.magnetizacion = magnetizacion
        self.tp = tp
        self.archivo = archivo
        
        # el metodo crea objetos
        if not any([b1, magnetizacion, tp]):
            self.extraer_resultados()
        else:
            print("Atencion! No se leyeron los resultados porque se forzo",
                  "el ingreso de 'b1', 'magnetizacion' o 'tp'. ")

    def extraer_resultados(self):
        """
        Este metodo extrae los resultados del archivo y los guarda en los
        atributos `b1` y ((( algo espacial para X Y ? ))). Ademas inicializa
        el objeto magnetizacion con las dimensiones n x 3: 
        n sitios, 3 componentes. Por otro lado, determina el tp utilizando el
        metodo del histograma (el Bxy con mayor ocurrencias).
        """
        # se usa asi:
        # [X, Y, Z, Bx, By, Bz] = self.extraer_resultados()
        print('leyendo archivo de datos...')
        resultados = np.loadtxt(self.archivo, comments='%', unpack=True)
        # elimino las filas que continenen NaN, para ello debo transponer.
        # luego, transpongo para regresar a su tamano original.
        resultados = resultados.transpose()
        resultados = resultados[~np.isnan(resultados).any(axis=1)]
        resultados = resultados.transpose()
        
        [X, Y, Bx, By, Bz] = resultados
        print("Resultados de '"+self.archivo+"' extraidos con exito.")
        
        # obtengo dim para pasarselos a M. lo transpongo para que sea nx3,
        # donde n es la cantidad de sitios
        dimensiones = np.array([Bx, By, Bz]).T.shape
        
        # creo los objetos campo y magnetizacion que son atributos de la clase
        self.b1 = Radiofrecuencia(Bx, By, Bz)
        self.magnetizacion = Magnetizacion(dimensiones)
        
        # estimo el tiempo de pulso
        self.b1.histograma()
        self.tp = np.pi/2 / self.b1.B90
               
        # el return se usa asi:
        # [X, Y, ...] = self.extraer_resultados()
        return resultados