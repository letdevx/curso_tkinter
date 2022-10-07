from ast import main
from cProfile import label
from cgitb import text
from curses import window
from tkinter import *
import tkinter
from turtle import left
from typing import Container 

def New():
    text_area.delete(1.0, "end")

def Save(): 
    container = text_area.get(1.0, "end")
    file = open("notepad.txt", "w")
    file.write(container)
    file.close()

def Open():
    file = open("notepad.txt", "r")
    container = file.read()
    text_area.insert(1.0, container)

window = tkinter.Tk()
window.title("Notpad")
window.minsize(width=1280, height=720)  

frame = tkinter.Frame(window, height=30)
frame.pack()

font_text =tkinter.Label(frame, text= "  Font:  ")
font_text.pack(side='left')

spin_font_size = tkinter.Spinbox(frame, values=("arial", "Verdana"))
spin_font_size.pack(side="left")

text_area = tkinter.Text(window, font="arial 20 bold", width=1280, height=720 )
text_area.pack(fill="x") #expade o item no eixo x

main_menu = tkinter.Menu(window)

file_menu = tkinter.Menu(main_menu, tearoff=0) 
file_menu.add_command(label="New", command= New)
file_menu.add_command(label="Save", command=Save)
file_menu.add_command(label="Open", command=Open)
file_menu.add_command(label="Exit", command=window.quit) 

main_menu.add_cascade(label="file", menu=file_menu)
window.config(menu=main_menu)





window.mainloop()