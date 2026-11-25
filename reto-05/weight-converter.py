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

#Funcion para convertir kg a gramos
def kg_to_grams():
    kg1=kg.get()
    grams=kg1 * 1000
    Label(window,text=f"{kg1} kg son {grams} gramos").pack()
    
#Funcion para convertir kg a libras
def kg_to_pounds():
    kg1=kg.get()
    pounds=kg1 * 2.20462
    Label(window,text=f"{kg1} kg son {pounds} libras").pack()
    

