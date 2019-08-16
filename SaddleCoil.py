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
            self.leer_archivo()
        
    def leer_archivo(self):
        print('leyendo archivo...')