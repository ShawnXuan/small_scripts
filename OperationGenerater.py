# -*- coding: utf-8 -*-
"""
Addition and Subtraction Operation Generater
Created on Wed May 17 16:43:40 2017

@author: ShwanXuan
"""
import numpy as np
from reportlab.pdfgen import canvas

question_number = 50 
cols = 5
rows = int(question_number/cols)

max_value = 100
terms_number = 2 

def GetQuestion(a, b, op):
    if(op):
        q = "%d + %d ="%(a,b)
        ans = a + b
    else:
        q = "%d - %d ="%(max(a,b),min(a,b))
        ans = max(a,b) - min(a,b)
    return q, ans

def Questions():
    x = np.random.randint(1, max_value, question_number)
    y = np.random.randint(1, max_value, question_number)
    Operation = np.random.choice([True, False],question_number)    
    for i in range(question_number):
        q, ans = GetQuestion(x[i],y[i],Operation[i])
        print(q)

Y_MAX = 780
LEFT_OFFSET = 40
Q_LENGTH = 110
A_LENGTH = 35
Q_LINE_OFFSET = 20
def PrintHeader(c, offset = 0):
    c.drawString(LEFT_OFFSET+40, Y_MAX-offset, "Date:______________    Start Time:__________    Finish Time:__________")

def PrintQuestionSet(c, qs, y_offset=0, x_offset=0):
    c.drawString(LEFT_OFFSET-10+x_offset, Y_MAX-y_offset, "QS:%s"%qs)

def PrintAQuestion(c, i, q, y_offset=0, x_offset=0):
    col = int(i/rows)
    row = i%rows
    s = "%d:  "%(i+1)
    x = LEFT_OFFSET+col*Q_LENGTH -10 + x_offset
    y = Y_MAX-row*Q_LINE_OFFSET-y_offset-Q_LINE_OFFSET
    c.drawString(x, y, s)
    x = x + 25
    c.drawString(x, y, q)
    
def PrintAnAnswer(c, i, q, y_offset=0, x_offset=0):
    col = int(i/rows)
    row = i%rows
    
    s = "%d:  "%(i+1)
    x = LEFT_OFFSET+col*A_LENGTH -10 + x_offset
    y = Y_MAX-row*Q_LINE_OFFSET-y_offset-Q_LINE_OFFSET
    if i<10:
        c.drawString(x-15, y, s)
        x = x + 5
    c.drawString(x, y, q)
    
if __name__ == '__main__':
    pages = 9
    cards_per_page = 3
    filename = "Question.pdf"
    c = canvas.Canvas(filename)
    filename = "Answer.pdf"
    ac = canvas.Canvas(filename)
    answer = np.zeros(question_number)
    for i in range(pages):
        if i%3==0 and i>0:
            print(i, type(i))
            ac.showPage()
        for j in range(cards_per_page):
            # question sheet
            y_offset = j*260
            PrintHeader(c, y_offset)
            PrintQuestionSet(c,"%d%d"%(i+1,j+1), y_offset)
            x = np.random.randint(1, max_value, question_number)
            y = np.random.randint(1, max_value, question_number)
            Operation = np.random.choice([True, False],question_number)    
            for k in range(question_number):
                q, ans = GetQuestion(x[k],y[k],Operation[k])
                answer[k]=ans
                PrintAQuestion(c, k, q, y_offset)
            # answer sheet
            index = j+i*cards_per_page
            
            y_offset = (i%3)*260
            x_offset = j * 190
            #print(index,y_offset,x_offset)
            PrintQuestionSet(ac,"%d%d"%(i+1,j+1), y_offset, x_offset)
            for k in range(question_number):
                PrintAnAnswer(ac, k, "%d"%answer[k], y_offset, x_offset)
        c.showPage()
        #print(i, type(i))
        
        
    c.save()
    ac.save()
    
