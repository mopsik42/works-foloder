import tkinter as tk

form = tk.Tk()
form.geometry('400x600+300+300')

frame = tk.Frame(form,background='gray',)
frame.pack(expand=True)

canvas = tk.Canvas(frame,width=250,height=250, background='black')
canvas.pack()
canvas.create_line(0,0,250,250,fill='red',width=5)  
canvas.create_rectangle(50,50,200,200,fill='blue',outline='yellow',width=5)
canvas.create_oval(50,50,100,200,fill='green',outline='yellow',width=5)
canvas.create_oval(100,50,150,200,fill='red',outline='green',width=5)
canvas.create_oval(150,50,200,200,fill='yellow',outline='red',width=5)
tk.mainloop()