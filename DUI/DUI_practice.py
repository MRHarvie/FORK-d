import tkinter as tk
from tkinter import ttk

def clicked_button1():
    first_window.title("Yes, I am the cool button")
    name = name_text.get()
    about_text.set(f"{name} is cool")

def clicked_button2():
    first_window.destroy()

first_window = tk.Tk()
first_window.title("My First GUI")
first_window.geometry("400x300")

frame = ttk.Frame(first_window, padding="10")
frame.pack(fill="both", expand=True)

name_label = tk.Label(frame, text="Name")
name_label.grid(row=0, column=0, sticky=tk.E)
#name_label.pack()
name_text = tk.StringVar()
name_entry = ttk.Entry(frame,width=25, textvariable=name_text)
name_entry.grid(row=0, column=1)
#name_entry.pack()
about_label = ttk.Label(frame,text="About")
about_label.grid(row=1, column=0,sticky=tk.E)
#about_label.pack()
about_text = tk.StringVar()
about_entry = ttk.Entry(frame,width=25, textvariable=about_text,state="readonly")
about_entry.grid(row=1,column=1)
#about_entry.pack()



button1 = ttk.Button(frame, text="I'm Cool", command=clicked_button1)
button1.grid(column=0,row=2)
button2 = ttk.Button(frame, text="No, I'm Cool",command=clicked_button2)
button2.grid(row=2,column=1)
#button1.pack()
#button2.pack()

for child in frame.winfo_children():
    child.grid_configure(padx=5,pady=3)


first_window.mainloop()
