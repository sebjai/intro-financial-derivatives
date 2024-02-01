# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:15:36 2023

@author: sebja
"""

from simulator import simulator
from pde import pde
import numpy as np

import matplotlib.pyplot as plt

from scipy.stats import norm


pde_obj = pde()

G = lambda x : (x>1)*np.cos(x)
sim_obj = simulator(G, 1)

g = pde_obj.solve(G)

# h = lambda t, x : norm.cdf((x-1)/np.sqrt(1-t))

def plot(i):
    
    g_hat = np.zeros(len(pde_obj.x))
    for j in range(len(pde_obj.x)):
        g_hat[j] = sim_obj.estimate(pde_obj.t[i], 
                                    pde_obj.x[j],
                                    batch_size=1_000)
        
    
    # plt.plot(pde_obj.x,h(pde_obj.t[i],pde_obj.x), linewidth=5,alpha=0.5)
    plt.plot(pde_obj.x, g[i,:])
    plt.scatter(pde_obj.x, g_hat, color='g', s=10)
    
    plt.show()
    
plot(0)