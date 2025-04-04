#!/usr/bin/env python3
import tkinter as tk 
from tkinter import messagebox

root = tk.Tk()
root.title("Menu() Widget")

def accion_menu():
    messagebox.showinfo("Menu", "se ha tensao la cosa")

barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu1 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Menu", menu=menu1)

menu1.add_command(label="opcion1")
menu1.add_command(label="opcion2")

menu2 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Extras", menu=menu2)

menu2.add_command(label="Se tensa", command=accion_menu)

root.mainloop()
