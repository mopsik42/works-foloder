import tkinter as tk
form=tk.Tk()
form.geometry('600x600')

canvas=tk.Canvas(width=500, height=500, bg="white")

canvas.create_rectangle(100,100,300,350, fill="MediumSpringGreen", width=3) # Тело

canvas.create_rectangle(130,130,270,200, fill="PaleGreen", width=1) # Лицо
canvas.create_oval(160,150,170,170, fill="black") # Лев глаз
canvas.create_oval(230,150,240,170, fill="black") # Прав глаз
canvas.create_arc(160,180,240,180, start=180, extent=180) # Рот

canvas.create_oval(140,210,220,220, fill="DarkGreen", width=3) # Зеленая полоска
canvas.create_oval(240,210,250,220, fill="MidnightBlue", width=3)
canvas.create_rectangle(150,240,160,270, fill="Gold", width=3)
canvas.create_rectangle(140,253,170,260, fill="Gold", width=3)
canvas.create_oval(220,240,240,260, fill="Cyan", width=3)
canvas.create_oval(250,260,270,280, fill="SeaGreen", width=3)
canvas.create_oval(210,280,240,310, fill="FireBrick", width=3)
canvas.create_oval(140,305,180,315, fill="Navy", width=3)

canvas.create_line(40,280,100,190, fill="black",width=4)
canvas.create_line(300,190,340,280, fill="black",width=4)
canvas.create_line(150,350,150,420, fill="black",width=4)
canvas.create_line(250,350,250,420, fill="black",width=4)



canvas.pack()
tk.mainloop()