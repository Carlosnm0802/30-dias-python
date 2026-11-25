#Importamos modulo tkinter
import tkinter as tk
from tkinter import *

#Elementos iniciales del proyecto 
window=Tk() #Creamos la ventana
window.title("Convertidor de Metricas")
window.geometry("500x500")
#Creamos un label
Label(window,text="METRIC CONVERTER", font=("Times new roman",20),bg="black",fg="yellow").pack()
kg = tk.IntVar() #kg es de tipo entero

