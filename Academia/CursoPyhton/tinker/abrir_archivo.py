#!/usr/bin/env python3

import tkinter as tk 
from tkinter import filedialog

root = tk.Tk()
root.geometry("200x70")

def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename()
    print(f"\n[+] Ruta del archivo en cuestion: {ruta_archivo}")

boton = tk.Button(root, text="Abrir archivo", command=abrir_archivo)
boton.pack(pady=15)

root.mainloop()
