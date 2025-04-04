#!/usr/bin/env python3

import tkinter as tk 

#grid() pack() place()

root = tk.Tk()
root.title("Metodo place()")
root.resizable(False, False)
label1 = tk.Label(root, text="Mi primer label", bg="red")
label2 = tk.Label(root, text="Mi segundo label", bg="green")
label3 = tk.Label(root, text="Mi tercer label", bg="blue")

label1.place(x=20, y=20)
label2.place(relx=0.8, rely=0.2)
label3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



root.mainloop()
