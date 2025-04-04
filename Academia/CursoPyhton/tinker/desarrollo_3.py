#!/usr/bin/env python3

import tkinter as tk 

root = tk.Tk()
root.title("Frame Widget")
root.resizable(False, False)
root.geometry("300x200")

frame = tk.Frame(root, bg="blue", bd=5)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label1 = tk.Label(frame, text="mi primer label", bg="green")
label2 = tk.Label(frame, text="mi segundo label", bg="red")

label1.pack(fill=tk.X)
label2.pack(fill=tk.X)

root.mainloop()



