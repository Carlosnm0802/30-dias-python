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
        
        #Format option
        self.output_format = StringVar(master)
        self.output_format.set(FORMATS[0])
        format_frame= ttk.Frame(master)
        format_frame.pack(pady=10)
        ttk.Label(format_frame, text="Select Output Format:").pack(side="left", padx=5)
        ttk.OptionMenu(format_frame, self.output_format, *FORMATS).pack(side="left")
        
        #Buttons
        ttk.Button(master, text="Resize & Compress", command=self.resize_images).pack(pady=10)
        ttk.Button(master, text="Convert Format", command=self.convert_images).pack(pady=10)
        
        #Footer
        ttk.Label(master, text="By Carlos Nares",font=("Arial", 8)).pack(side="bottom", pady=10)
        
    def select_files(self):
        self.selected_files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.webp")]
        )
        if self.selected_files:
            messagebox.showinfo("Selected Files", f"{len(self.selected_files)} files selected.")
        else:
            messagebox.showwarning("No Files Selected", "No files were selected.")
        
    def resize_images(self):
        if not self.selected_files:
            messagebox.showwarning("No Files Selected", "Please select images first.")
            return
        width = simple_prompt("Enter width in pixels")
        height = simple_prompt("Enter height in pixels")
        quality = simple_prompt("Enter compression quality (1-95)",default="80")
        if not (width and height and quality):
            return 
        try:
            width,height,quality = int(width), int(height), int(quality)
        except ValueError:
            messagebox.showerror("Invalid Input", "Width, height, and quality must be integers.")
            return 
        output_dir = filedialog.askdirectory(title="Select Output Folder")
        if not output_dir:
            return
        
        for file in self.selected_files:
            try:
                img = Image.open(file)
                img_resized = img.resize((width, height))
                file_name = os.path.splitext(os.path.basename(file))[0]
                output_path = os.path.join(output_dir, f"{file_name}_resized.jpg")
                img_resized.save(output_path, "JPEG", quality=quality)
            except Exception as e:
                print(f"Error processing file {file}: {e}")
                
        messagebox.showinfo("Process Completed", "Image resizing completed.")
        