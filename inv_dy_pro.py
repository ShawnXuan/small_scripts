# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:25:58 2017

@author: xiex
"""

import numpy as np

fkx = np.array([[0,  0,  0,  0 ],
                [11, 0,  2,  20],
                [12, 5,  10, 21],
                [13, 10, 30, 22],
                [14, 15, 32, 23],
                [15, 20, 40, 24]],dtype=np.int16 )
Fkx = np.zeros(fkx.shape,dtype=np.int16)
xkx = np.zeros(fkx.shape,dtype=np.int16)
Fkx[:,0] = fkx[:,0]
xkx[:,0] = range(fkx.shape[0])
for k in range(1, fkx.shape[1]):
    for x in range(1, fkx.shape[0]):
        for xk in range(x+1):
            if (fkx[xk,k]+Fkx[x-xk,k-1]) > Fkx[x,k]:
                Fkx[x,k] = fkx[xk,k]+Fkx[x-xk,k-1]
                xkx[x,k] = xk
                
m = int(5)
n = 4
print("Total investment income:", Fkx[m, n-1])
for i in reversed(range(n)):
    print("Invest",xkx[m,i],"on project", i+1)
    m = m - xkx[m,i]

