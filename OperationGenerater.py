# -*- coding: utf-8 -*-
"""
Addition and Subtraction Operation Generater
Created on Wed May 17 16:43:40 2017

@author: ShwanXuan
"""
import numpy as np

max_value = 100
terms_number = 2 
question_number = 100 

x = np.random.randint(1, max_value, question_number)
y = np.random.randint(1, max_value, question_number)
Operation = np.random.choice([True, False],100)


def GetQuestion(a, b, op):
    if(op):
        q = "%.2d + %.2d = "%(a,b)
        ans = a + b
    else:
        q = "%.2d - %.2d = "%(max(a,b),min(a,b))
        ans = max(a,b) - min(a,b)
    return q, ans
            
for i in range(100):
    q, ans = GetQuestion(x[i],y[i],Operation[i])
    print(q)
