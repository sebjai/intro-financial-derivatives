# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:01:54 2023

@author: sebja
"""

import numpy as np

import pdb

class pde():
    
    def __init__(self, T=1, Ndt=101):
        
        self.T = T
        self.Ndt = Ndt
        
        # set the t grid
        self.t = np.linspace(0,self.T, self.Ndt)
        self.dt = self.t[1]-self.t[0]
        
        
        # set the x-grid
        self.dx = np.sqrt(3*self.dt)
        
        self.max_x = 10*np.sqrt(self.T)
        self.min_x = -10*np.sqrt(self.T)
        
        self.Ndx = int((self.max_x-self.min_x)/self.dx)
        
        self.x = np.linspace(self.min_x, self.max_x, self.Ndx)
        self.dx = self.x[1]-self.x[0]
        
        
    def solve(self, G):
        
        g = np.zeros((len(self.t), len(self.x)))
        
        # set terminal condition
        g[-1,:] =G(self.x)
        
        for i in range(self.Ndt-1,0,-1):
            
            ddg = (g[i, 2:] - 2*g[i,1:-1] + g[i, :-2])/self.dx**2
            
            g[i-1, 1:-1] = g[i,1:-1] + self.dt*0.5*ddg
            
            g[i-1,0] = 2*g[i-1,1] - g[i-1,2]
            g[i-1,-1] = 2*g[i-1,-2] - g[i-1,-3]
            
        return g
            
            
            