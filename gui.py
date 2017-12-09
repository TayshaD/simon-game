import tkinter as tk
from time import sleep
from random import randint;


#sequence length cap
max_seq_length = 20
#necessary game variables
strict_mode = False
sequence = []
user_moves = []
user_turn = False
game_started = False
#variables for display text
mode_label_text = "Strict OFF"
counter_label_text = "--"

#colors for game display in rgby order
colors = ["#dd4b3e", "#3edd4b", "#4b3edd", "#ffea37"]
active_colors = ["#e47267", "#7de886", "#7267e4", "#fff280"]

#functions to make a button "flash"
#blinkon will change a button's fill to its active color
#blinkon returns it to a normal state
#flash blinks on, then blinks off after short delay
#//TODO: add sound effects?

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
def flash (id, delay=3000):
    blinkOn(id)
    root.update()
    root.after(delay, blinkOff(id))

#generates the random sequence of buttons using their ids
#sequence is as long as the pre-specified max sequence length
def generate_seq():
    for x in range(max_seq_length):
        sequence.append(randint(0,3))

#toggles strict mode on and off
def toggle_strict(event):
    global strict_mode, mogameHasStartede_label, mode_label_text
    strict_mode = not strict_mode
    mode_label_text = "Strict ON" if strict_mode else "Strict OFF"
    canvas.itemconfigure(mode_label, text=mode_label_text)

#updates the counter based on input parameter
#if you input 0, that will reset the counter
#else, it will increment the counter if the game has startd
def update_counter(operation):
    global counter_label_text, count, game_started
    if (operation == 0):
        counter_label_text = 0;
    elif (game_started):
        counter_label_text = str(int(counter_label_text) + 1)
    canvas.itemconfigure(count, text=counter_label_text)

#function to display the sequence of buttons
def display_seq():
    global sequence, counter_label_text, game_started, user_turn
    if game_started:
        current_count = int(counter_label_text);
        for x in range(current_count+1):
            flash(sequence[x])
        user_turn = True;


def start_game():
    global game_started
    if (not game_started):
        game_started = True
        update_counter(0)
        generate_seq()
        for x in range(4):
            flash(x, 2000)
def game_on():
    pass

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
mode_label = canvas.create_text(475, 325, font=("Impact", 20), text = mode_label_text, fill="white")

canvas.tag_bind(mode_label, '<ButtonPress-1>', toggle_strict)

"""issue! even when using tag binds or explicit delays, the program always starts the game immediately upon execution. I've just given up on having any built-in delay for now, but optimal thing would be to get that working"""
start_game()
root.after(3000, display_seq)
root.mainloop()
