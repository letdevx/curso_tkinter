from cProfile import label
from distutils.cmd import Command
from tkinter import *
import tkinter
from turtle import left

linhas = []

window = tkinter.Tk()
window.title("Seguro")
window.minsize(width=300, height=400)  
window.configure()

placa = Label(window, text = "Placa (XXX-0000)").grid(row = 0, column=0)
placa_input = Entry(window)
placa_input.grid(row = 0, column = 1)

modelo = Label(window, text="Modelo/Ano").grid(row=1, column=0)
modelo_input = Entry(window)
modelo_input.grid(row = 1, column = 1)

idade = Label(window, text="Idade").grid(row= 2, column=0)
idade_input = Entry(window)
idade_input.grid(row = 2, column =1 )

valor = Label(window, text="valor base").grid (row=3, column=0)
valor_input= Entry(window)
valor_input.grid(row=3, column=1) 

def set_text(entry, text):
    entry.delete(0,tkinter.END)
    entry.insert(0,text)

def Save(): 
    container = f"{placa_input.get()};{modelo_input.get()};{idade_input.get()};{valor_input.get()}\n"
    file = open("cadastro_seguro.txt", "a")
    file.write(container)
    file.close()

def Open():
    file = open("cadastro_seguro.txt", "r")
    container = file.read(1.0, "end")
    file.writelines(container) 

def leArquivo():
    global linhas
    file = open("cadastro_seguro.txt", "r")
    texto = file.read()
    quebraLinha = "\n"
    linhas = texto.split(quebraLinha) 


def pesquisa(placa):
    for i, linha in enumerate(linhas):
        campos = linha.split(";")
        if(placa == campos[0]):
            return campos 



def preenche_campos(campos):
    global valor_input
    global idade_input
    global modelo_input
    global placa_input
    set_text(placa_input, campos[0]) 
    set_text(modelo_input, campos[1])
    set_text(idade_input, campos[2])
    set_text(valor_input, campos[3]) 


def listar_click():
    global placa_input
    leArquivo()
    campos = pesquisa(placa_input.get())
    preenche_campos(campos)





botao1 = Button(window,text="Gravar",command=Save)
botao1.grid (row = 4 , column = 0) 

botao1 = Button(window,text="Listar p/ Placa",command=listar_click)
botao1.grid (row = 4 , column = 1) 




window.mainloop()