import tkinter as tk
from time import sleep
from random import randint;
#sequence length cap
max_seq_length = 20
#necessary game variables
strictMode = False
sequence = []
userMoves = []
userTurn = False
mode_label_text = "Strict OFF"
counter_label_text = "--"
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

#generates the random sequence of buttons using their ids
#sequence is as long as the pre-specified max sequence length
def generateSeq():
    for x in range(max_seq_length):
        sequence.append(randint(0,3))

#toggles strict mode on and off
def toggleStrict(event):
    global strictMode, mode_label, mode_label_text
    strictMode = not strictMode
    mode_label_text = "Strict ON" if strictMode else "Strict OFF"
    canvas.itemconfigure(mode_label, text=mode_label_text)

#updates the counter based on input parameter
#if you input 0, that will reset the counter
#else, it will increment the counter if the game has startd
def updateCounter(operation):
    global counter_label_text, count
    if (operation == 0):
        counter_label_text = 0;
    elif (counter_label_text != "--"):
        counter_label_text = str(int(counter_label_text) + 1)
    canvas.itemconfigure(count, text=counter_label_text)


root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

#-----------------------------these are the buttons-------------------------------------
green = canvas.create_rectangle(2, 2, 400, 300, fill=colors[1], activefill=active_colors[1], width=2)

yellow = canvas.create_rectangle(2, 300, 400, 600, fill=colors[3],activefill=active_colors[3], width=2)

red = canvas.create_rectangle(400,2,800, 300, fill=colors[0], activefill=active_colors[0], width=2)

blue = canvas.create_rectangle(400, 300, 800, 600, fill=colors[2], activefill=active_colors[2], width=2)

center = canvas.create_rectangle(200, 225, 601, 376,

outline="#aaaaaa", width=2, fill="black")
title = canvas.create_text(400, 275, font=("Impact", 30, 'bold'), text="SIMON", fill="white")

#this is the counter and strict toggle button
counter_label = canvas.create_text(300, 325, font=("Impact", 20), text="SCORE:", fill="white")
count = canvas.create_text(375, 325, font=("Impact", 20), text=counter_label_text, fill="red")
mode_label = canvas.create_text(475, 325, font=("Impact", 20), text = mode_label_text, fill="white", tags="strictToggle")
canvas.tag_bind(mode_label, '<ButtonPress-1>', toggleStrict)



root.mainloop()
