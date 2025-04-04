#!/usr/bin/env python3

import tkinter as tk 

root = tk.Tk()
root.geometry('200x100')
root.title("entry() widget")
root.resizable(False, False)

def get_data():
    data = entry_widget.get()
    print(f"\n[+]datos introducidos {data}")

entry_widget = tk.Entry(root)
entry_widget.pack(pady=3, padx=15, fill=tk.X)

buton = tk.Button(root, text="Recoger entrada", command=get_data)
buton.pack(padx=15, fill=tk.X)

root.mainloop()
