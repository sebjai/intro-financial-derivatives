# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:02:19 2024

@author: sebja
"""

import numpy as np


class simulator():
    
    def __init__(self, G, T):
        
        self.G = G
        self.T = T
        
    def estimate(self, t, x, batch_size=1_000):
        
        
        X_T = x + np.sqrt(self.T-t)*np.random.randn(batch_size)
        
        g = np.mean(self.G(X_T))
        
        return g
        
    
    