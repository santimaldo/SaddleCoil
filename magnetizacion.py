# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:14:22 2019

@author: santi
"""
import numpy as np

class Magnetizacion:
    
    
    def __init__(self, dimensiones):
        
        self.M0 = np.array([0,0,1])
        self.M = np.zeros(dimensiones)
        # debo transponer para poder desempaquetar.
        self.Mx, self.My, self.Mz = self.M.transpose()
    
    def set_M(self, M):
        self.M = M
        self.Mx, self.My, self.Mz = self.M.transpose()