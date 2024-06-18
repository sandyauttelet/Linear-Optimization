"""

@author: sandy

"""

import tkinter as tk
from tkinter import filedialog
import csv
import os
from ctypes import windll
import numpy as np

"""
===================================================================================
This file is for creating a GUI if user wants to input data into a text file named
input_data.txt.

Files will be overwritten so ensure this does not happen if you want to save
many data inputs by changing save name from input_data to another name, or save
data in a different location.

Errors can occur if directory is not corrected so ensure you have saved input_data
to desired directory with os.chdir() to change saving location.

This GUI has not been tested nor will it determine input errors. All errors will
present themselves when running the main file.

Window must be closed to proceed through the computation.
===================================================================================
"""

#os.getcwd() #Check your current directory path

#Change directory to save to another location
os.chdir('C:/Users/sandy/OneDrive/Documents/Classes/Math 464- Lin Opt/Final Project/data')

window = tk.Tk()

my_data = []

window.geometry("800x800")
window.title("User Inputs for Optimal Path Calculation")

title_frame = tk.Frame(master=window,relief=tk.RAISED, borderwidth=10, height=400, bg="white")
title_frame.pack(fill=tk.X)
title = tk.Label(title_frame, text="Please input user data to find the optimal path to travel.", bg="white")
title.pack(padx=(5, 5), pady=5)

frame1 = tk.Frame(master=window,relief=tk.RAISED, borderwidth=10, height=100)
frame1.pack(fill=tk.X)

sourceframe = tk.Frame(master=window,relief=tk.RAISED, borderwidth=10, height=50, bg='#FF19FF')
sourceframe.pack(fill=tk.X)

sinkframe = tk.Frame(master=window,relief=tk.RAISED, borderwidth=10, height=25, bg='#B3FFFF')
sinkframe.pack(fill=tk.X)

frame2 = tk.Frame(master=window,relief=tk.RAISED, borderwidth=10, height=100)
frame2.pack(fill=tk.X)

graph1_val = tk.StringVar()
graph2_val = tk.StringVar()
source_val = tk.StringVar()
sink_val = tk.StringVar()
weight_val = tk.DoubleVar()
tol1_val = tk.DoubleVar()
tol2_val = tk.DoubleVar()
cost_val = tk.DoubleVar()

graph1_entry = tk.Entry(frame1, textvariable=graph1_val, fg="black", bg="white", width=30)
graph1_label = tk.Label(frame1, text="Distance Data Set:\n(include file type i.e. distance.csv)")
graph1_label.grid(row=0, column=0, padx=(5, 5), pady=5)

graph2_entry = tk.Entry(frame1, textvariable=graph2_val, fg="black", bg="white", width=30)
graph2_label = tk.Label(frame1, text="Delay Data Set:\n(include file type i.e. delay.csv)")
graph2_label.grid(row=1, column=0, padx=(5, 5), pady=5)

source_entry = tk.Entry(sourceframe, textvariable=source_val, fg="black", bg="white", width=40)
source_label = tk.Label(sourceframe, text="Starting City:", bg="white")
source_label.grid(row=0, column=0, padx=(5, 5), pady=5)

sink_entry = tk.Entry(sinkframe, textvariable=sink_val, fg="black", bg="white", width=41)
sink_label = tk.Label(sinkframe, text="Ending City:",bg="white")
sink_label.grid(row=0, column=0, padx=(5, 5), pady=5)

weight_entry = tk.Entry(frame2, textvariable=weight_val, fg="black", bg="white", width=30)
weight_label = tk.Label(frame2, text="Delay Importance:")
weight_label.grid(row=0, column=0, padx=(5, 5), pady=5)

tol1_entry = tk.Entry(frame2, textvariable=tol1_val, fg="black", bg="white", width=30)
tol1_label = tk.Label(frame2, text="Max Time of Delivery [hours]:")
tol1_label.grid(row=1, column=0, padx=(5, 5), pady=5)

tol2_entry = tk.Entry(frame2, textvariable=tol2_val, fg="black", bg="white", width=30)
tol2_label = tk.Label(frame2, text="Max Risk Willing to Occur [$]:")
tol2_label.grid(row=2, column=0, padx=(5, 5), pady=5)

cost_entry = tk.Entry(frame2, textvariable=cost_val, fg="black", bg="white", width=30)
cost_label = tk.Label(frame2, text="Cost of Order [$]:")
cost_label.grid(row=3, column=0, padx=(5, 5), pady=5)

graph1_entry.grid(row=0, column=1,padx=10,pady=10)
graph2_entry.grid(row=1, column=1,padx=10,pady=10)
source_entry.grid(row=0,column=1,padx=10,pady=10)
sink_entry.grid(row=0,column=1,padx=10,pady=10)
weight_entry.grid(row=0,column=1,padx=10,pady=10)
tol1_entry.grid(row=1,column=1,padx=10,pady=10)
tol2_entry.grid(row=2,column=1,padx=10,pady=10)
cost_entry.grid(row=3,column=1,padx=10,pady=10)


def save_info():
    tk.messagebox.showinfo(title="Submit successful", message="Data submitted succesfully. Report and plots will print in terminal.")
    graph1 = graph1_entry.get()
    graph2 = graph2_entry.get()
    source = source_entry.get()
    sink = sink_entry.get()
    weight = weight_entry.get()
    tol1 = tol1_entry.get()
    tol2 = tol2_entry.get()
    cost = cost_entry.get()
    
    file = open("input_data.txt", "w")
    file.write(graph1)
    file.write(",")
    file.write(graph2)
    file.write(",")
    file.write(source)
    file.write(",")
    file.write(sink)
    file.write(",")
    file.write(weight)
    file.write(",")
    file.write(tol1)
    file.write(",")
    file.write(tol2)
    file.write(",")
    file.write(cost)
    file.close()
    window.destroy()
    
        

file_path = None
submit_button = tk.Button(window,
    text="Submit Data",
    command=save_info,
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

submit_button.pack(padx=20,pady=20)


def on_closing():
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()

def load_data():
    data = np.genfromtxt('input_data.txt', dtype=None, delimiter=",", encoding=None)
    
    file1_name = str(data['f0'])
    file2_name = str(data['f1'])
    source = str(data['f2'])
    sink = str(data['f3'])
    weight = data['f4']
    tol = []
    tol.append(data['f5'])
    tol.append(data['f6'])
    order_cost = data['f7']
    file1_text = file1_name.split(".")
    file2_text = file2_name.split(".")
    return file1_name,file2_name, source, sink, weight, tol, order_cost, file1_text[0], file2_text[0], file1_text[1], file2_text[1]
