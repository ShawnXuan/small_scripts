# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 08:34:25 2017

@author: xiex
"""

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
#from numpy import arange
#import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
#from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
# Hyper Parameters
TrainLength = 250.0
a = 1.0
speed = 601.2/3.6 # 167m/s
deltaT = 0.5 #time steps
duration = 400 #simlation time +-10 minutes

departure_switch_speed = 100/3.6
departure_s = departure_switch_speed*departure_switch_speed/2/a
arrival_switch_speed = 200/3.6
arrival_s = -arrival_switch_speed*arrival_switch_speed/2/a
    
class train:
    def __init__(self, master, id, offset=0, stop=True, dwell=90):
        tk.Label(master, text='Train %d:'%id).grid(row=id, column=0)
        self.txt_offset = tk.IntVar()
        self.txt_offset.set(offset) 
        self.train_offset = tk.Entry(master, width=16, textvariable=self.txt_offset)
        self.train_offset.grid(row=id, column=1)
        
        self.ck_stop = tk.IntVar()
        self.ck_stop.set(stop)
        self.train_stop = tk.Checkbutton(master, variable=self.ck_stop, onvalue=1, offvalue=0, command=self.StopOrNot)
        self.train_stop.grid(row=id, column=2)
        #self.ck_stop.set(stop)
        
        self.txt_dwell = tk.IntVar()
        self.txt_dwell.set(dwell) 
        self.train_dwell = tk.Entry(master, width=16, textvariable=self.txt_dwell)
        self.train_dwell.grid(row=id, column=3)
        if not stop:
            self.train_dwell.configure(state='disabled')
        #self.t = arange(0.0, duration, deltaT)
        
        #self.platform_stop = stop #train will stop at the platform in default
        #self.dwell = dwell #default dwell time 
        #self.offset = offset #default time offset 
        #self.init_profile()
    def StopOrNot(self):
        stop = self.ck_stop.get()
        if stop:
            self.train_dwell.configure(state='normal')
        else:
            self.train_dwell.configure(state='disabled')
        
    def init_profile(self):
        platform_stop = self.ck_stop.get()
        dwell = self.txt_dwell.get()
        offset = self.txt_offset.get()
        print(platform_stop, dwell, offset)
        if platform_stop==1:
            t_ = np.arange(0.0, duration+speed/2/a, deltaT)
            s_ = 0.5*a*t_*t_
            at = speed/a
            s_[t_>at]=0.5*a*at*at+speed*(t_[t_>at]-at)
            
            _t = -t_
            _t.sort()
            _s = -s_
            _s.sort()
            if dwell > 0:
                t_=t_+ dwell
                
            t_ = t_+ speed/2/a
            _t = _t+ speed/2/a
                
        else:
            t_ = np.arange(0.0, duration, deltaT)
            s_ = t_ * speed
            _t = -t_
            _t.sort()
            _s = -s_
            _s.sort()
        self.t = np.concatenate((_t,t_))+offset * 60
        self.s = np.concatenate((_s,s_))
        
    def plot(self, ax):
        self.init_profile()
        self.head, = ax.plot(self.s, self.t,'r')
        self.tail, = ax.plot(self.s-TrainLength, self.t,'g')
            
        
def plot_trains():
    global ax, f
    global train1, train2, train3, train4

    #for i, line in enumerate(ax.lines):
    for i in reversed(range(len(ax.lines))):
        ax.lines.pop(i)
        #line = ax.lines[i]
    #print(len(ax.lines))
        
    train1.plot(ax)
    train2.plot(ax)
    train3.plot(ax)
    train4.plot(ax)
    
    ad = np.array([arrival_s, 0, departure_s, 10000, 30000,50000,-16000, -36000,-56000])
    #xticks = ax.get_xticks()
    #xticks = np.concatenate((xticks,ad))
    #ax.set_xticks(xticks)
    ax.set_xticks(ad)
    f.canvas.draw()

    
win = tk.Tk()
win.title('Headway Analysis for Maglev')
win.geometry('800x1000')

frm_main = tk.Frame(win)
frm_main.pack()

frm_trains = tk.Frame(frm_main)
frm_trains.pack(side='top')

# row 0
b_replot=tk.Button(frm_trains, text='Plot', width='10',command=plot_trains)
b_replot.grid(row=0, column=0)
tk.Label(frm_trains, text='Time Offset(min)').grid(row=0, column=1)
tk.Label(frm_trains, text='Stop').grid(row=0, column=2)
tk.Label(frm_trains, text='Dwell Time(sec)').grid(row=0, column=3)

train1 = train(frm_trains, 1, offset=-4, stop=True, dwell=313)
train2 = train(frm_trains, 2, offset=0,  stop=False, dwell=0)
train3 = train(frm_trains, 3, offset=4, stop=True, dwell=313)
train4 = train(frm_trains, 4, offset=8, stop=False, dwell=0)

frm_plot = tk.Frame(frm_main)
frm_plot.pack(side='bottom')

f = Figure(figsize=(16, 8), dpi=100)

#f, ax = plt.subplots()
ax = f.add_subplot(111)
ax.grid(True)


#plot_trains()
train1.plot(ax)
train2.plot(ax)
train3.plot(ax)
train4.plot(ax)
#f.clf()

#xticks = ax.get_xticks()
#==============================================================================
# ad = np.array([arrival_s, departure_s])
# xticks = ax.get_xticks()
# xticks = np.concatenate((xticks,ad))
# ax.set_xticks(xticks)
#==============================================================================
#ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=frm_plot)
canvas.show()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, frm_plot)
toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

win.mainloop()      

