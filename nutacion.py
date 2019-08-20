# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:03:27 2019

@author: santi
"""
import numpy as np
from scipy.interpolate import interp1d

class Nutacion:
    """
    Esta clase contiene la información de la simulacion de la nutacion. Se
    encarga de interpolar los valores simulados de nutacion para obtener 
    valores como el tiempo de pulso de 90.
    
    Attributes
    ----------
    tp_list: array 1D
        Tiempos de pulso utilizados para la nutación
    
    signal : array 1D
        Valores de denal obtenidos en la nutación
    
    tp_list_interpol: array 1D
        1000 valores de tiempo equiespaciados entre 0 y el último valor de 
        `tp_list`.
    
    signal_interpol : array 1D
        Interpolacion de `signal` utilizando 1000 puntos. El método utlizado es
        el de interpolación cúbica.
        
    tp90 : float
        Valor de tiempo asociado al máximo de `signal_interpol`. Corresponde al
        valor de tp al cual se le asocia un pulso de 90°.
        
    Methods
    -------
    get_max()
        Método que se encarga de interpolar y obtener `tp90`. La interpolación
        utiliza la función interp1d del módulo scipy.interpolate.
    
    get_tp90()
        Devuelve el tiempo de pulso asociado al pulso de 90°.
        
    """
    
    # Atributos:
    tp_list = None
    signal = None
    tp_list_interpol = None
    signal_interpol = None
    tp90 = None   
    
    
    def __init__(self, tp_list, signal):
        
        self.tp_list = tp_list
        self.signal = signal
        
        self.get_max()
        
    def get_max(self):
        
        # interpolacion de la nutacion.
        S_interpol = interp1d(self.tp_list, self.signal, kind='cubic')
        
        # S_interpol, la interpolacion de la nutacion, se usa como funcion.
        tp = np.linspace(0, self.tp_list[-1], 1000)
        S = S_interpol(tp)
        
        # Busco el maximo de la nutacion para determinar el pulso de 90.
        max_index = np.argmax(S)
        tp90 = tp[max_index]
        
        # guardo en atributos
        self.tp_list_interpol = tp
        self.signal_interpol = S
        self.tp90 = tp90
        
        return 0
    
    def get_tp90(self):
        return self.tp90
        
        