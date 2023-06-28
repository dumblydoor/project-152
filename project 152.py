#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 15:13:58 2023

@author: aquilavijayanayagam
"""

import matplotlib.pyplot as plt

data=[[0,0,0,0,0,0,0,0],
      [0,0,1,1,1,1,0,0],
      [0,0,1,0,0,1,0,0],
      [0,0,1,0,0,1,0,0],
      [0,0,1,0,0,1,0,0],
      [0,0,1,0,0,1,0,0],
      [0,0,1,1,1,1,0,0],
      [0,0,0,0,0,0,0,0]]
      
plt.imshow(data,cmap='gray')
     