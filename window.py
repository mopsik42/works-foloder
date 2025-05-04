import tkinter as tk
from tkinter import messagebox

def msg():
    name = txt1.get()
    sname = txt2.get()
    messagebox.showerror("Title",f'пользователь {name} {sname}')

wind=tk.Tk()
wind.title("Моя программа")
wind.geometry("500x500")
tk.Label(wind,text="введите имя").pack()
txt1 = tk.Entry(wind)
txt1.pack()
tk.Label(wind,text="введите фамилию").pack()
txt2=tk.Entry(wind)
txt2.pack()
tk.Button(wind,text="tap",command=msg).pack(pady=5)


wind.mainloop()