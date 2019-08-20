# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:02:59 2019

@author: santi
"""
import numpy as np

class Senal:
    """
    Esta clase contiene la información de la Senal dada una magnetización.
    Se encarga de obtener el modulo y la fase de la magnetización el plano xy.
    
    Attributes
    ----------
    Sx: array 1D
        Es la magnetización en el eje x.
    
    Sy: array 1D
        Es la magnetización en el eje y.
    
    senal_total: float
        Amplitud de la suma vectorial sobre todos los sitios, de la 
        magnetización en en el plano xy.
    
    fase : float
        Fase (ángulo respecto a x) de la suma vectorial sobre todos los sitios, de la 
        magnetización en en el plano xy.        
        
    Methods
    -------
    sumatoria()
        Suma vectorial de la magnetizacion sobre todos los sitios. Setea el 
        valor de `senal_total` y de `fase`.
    
    get_total()
        Devuelve el el valor de `senal_total`
        
    """
    
    def __init__(self, magnetizacion):
        
        # M es un objeto de la clase Magnetizacion
        self.Sx = magnetizacion.Mx
        self.Sy = magnetizacion.My
        self.senal_total = None
        self.fase = None
        self.sumatoria()
        
    def sumatoria(self):
        Sx = np.sum(self.Sx)
        Sy = np.sum(self.Sy)

        Sxy = Sx + 1j * Sy
    
        self.senal_total = np.abs(Sxy)
        self.fase = np.angle(Sxy)
        return 0
    
    def get_total(self):
        return self.senal_total
    
    