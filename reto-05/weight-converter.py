#Importamos modulo tkinter
import tkinter as tk
from tkinter import *

#Elementos iniciales del proyecto 
window=Tk() #Creamos la ventana
window.title("Convertidor de Metricas")
window.geometry("600x800")
window.config(bg="#2d2d2d")
#Creamos un label
Label(window,text="METRIC CONVERTER", font=("Times new roman",20,"bold"),bg="black",fg="yellow",pady=10).pack(fill=tk.X)
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
#Funcion para convertir kg a onzas
def kg_to_ounces():
    kg1=kg.get()
    ounces=kg1 * 35.274
    Label(window,text=f"{kg1} kg son {ounces} onzas").pack()

#Labels para ingresar valores
Label(window,text="Ingrese el peso en kg:",font=("Arial",14,"bold"),bg="#2d2d2d",fg="#ffffff").pack(pady=(30,10))
Entry(window,textvariable=kg,font=("Arial",14),width=20,bd=2,bg="#444444",fg="#ffffff",insertbackground="#ffffff").pack(pady=(0,40))

#Creamos los botones
Button(window,text="Convertir a gramos",command=kg_to_grams,font=("Arial",13,"bold"),bg="#4CAF50",fg="white",padx=20,pady=15).pack(pady=10,fill=tk.X,padx=40)
Button(window,text="Convertir a libras",command=kg_to_pounds,font=("Arial",13,"bold"),bg="#2196F3",fg="white",padx=20,pady=15).pack(pady=10,fill=tk.X,padx=40)
Button(window,text="Convertir a onzas",command=kg_to_ounces,font=("Arial",13,"bold"),bg="#FF9800",fg="white",padx=20,pady=15).pack(pady=10,fill=tk.X,padx=40)

#Iniciamos el loop de la ventana
window.mainloop()