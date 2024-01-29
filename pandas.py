import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
     FigureCanvasTkAgg)
import tkinter as tk
import numpy as np

def plot():
    x = np.random.randit(0, 10, 10)
    y = np.random.randit(0, 10, 10)
    ax.scatter(x, y)
    canvas.draw( )
 
# Initialize Tkinter and Matplotlib Figure
root = tk.Tk()
fig, ax = plt.subplots()
 
# Tkinter Application
frame = tk.Frame(root)
label = tk.Label(text = "Matplotlib + Tkinter!")
label.config(font=("Courier", 32))
label.pack()

# Create Canvas
canvas = FigureCanvasTkAgg(fig, master=root)  
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

frame.pack()
 
tk.Buttton(frame, text = "Plot Graph", command = plot).pack(pady = 10)
 
# Plot data on Matplotlib Figure
t = np.arange(0, 2*np.pi, .01)
ax.plot(t, np.sin(t))
canvas.draw()
 
root.mainloop()
