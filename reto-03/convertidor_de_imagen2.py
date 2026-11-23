import os
from tkinter import filedialog, Tk, messagebox, StringVar
from tkinter import ttk
from PIL import Image

#Formatos soportados
FORMATS = ['JPG', 'PNG', 'WEBP']

class ImageConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Converter Tool")
        master.geometry("400x350")
        master.configure(bg="#f7f7f7")
        master.resizable(False, False)
        
        self.selected_files = []
        
        #Style
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc", font=("Arial", 10))
        style.configure("TLabel", background="#f7f7f7", font=("Arial", 10))
        style.configure("TOptionMenu", background="#f7f7f7", font=("Arial", 10))
        style.configure("Title.TLabel", background="#f7f7f7", font=("Arial", 14, "bold"))
        
        #Title
        ttk.Label(master, text="Image Converter Tool", style="Title.TLabel").pack(pady=20)
        
        #Select images
        ttk.Button(master, text="Select Images", command=self.select_images).pack(pady=10)