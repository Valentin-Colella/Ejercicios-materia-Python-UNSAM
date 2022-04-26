# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:24:41 2021

@author: HP
"""
import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.load('../Data/Temperaturas.npy')
plt.hist(temperaturas,bins=25)
