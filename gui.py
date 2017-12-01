import tkinter as tk
from time import sleep
#colors for game display in rgbyg order
colors = ["#dd4b3e", "#3edd4b", "#4b3edd", "#ffea37"]
active_colors = ["#e47267", "#7de886", "#7267e4", "#fff280"]

#functions to make a button "flash"
def getTarget(id):
    target = None
    if (id == 0):
        target = red
    elif id == 1:
        target = green
    elif id == 2:
        target = blue
    else:
        target = yellow
    return target
def blinkOn(id):
    target = getTarget(id)
    canvas.itemconfig(target, fill=active_colors[id])
def blinkOff(id):
    target = getTarget(id)
    canvas.itemconfig(target, fill=colors[id])
def flash (id):
    blinkOn(id)
    root.update()
    root.after(3000, blinkOff(id))


root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()


green = canvas.create_rectangle(2, 2, 400, 300, fill=colors[1], activefill=active_colors[1], width=2)

yellow = canvas.create_rectangle(2, 300, 400, 600, fill=colors[3],activefill=active_colors[3], width=2)

red = canvas.create_rectangle(400,2,800, 300, fill=colors[0], activefill=active_colors[0], width=2)

blue = canvas.create_rectangle(400, 300, 800, 600, fill=colors[2], activefill=active_colors[2], width=2)

center = canvas.create_rectangle(200, 225, 601, 376,

outline="#aaaaaa", width=2, fill="black")
title = canvas.create_text(400, 275, font=("Impact", 30, 'bold'), text="SIMON", fill="white")

root.mainloop()
