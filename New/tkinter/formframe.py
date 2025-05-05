import tkinter as tk
from tkinter import messagebox as msgbox

form = tk.Tk()
form.title("FormFrame")
form.geometry("400x600")
form.resizable(False, False) # не разрешаем изменять размер окна
form.config(bg="#f0f0f0")   # цвет фона
form.iconphoto(False, tk.PhotoImage(file="New/tkinter/image.png"))  # иконка окна
form.attributes("-topmost", True)  # Окно всегда сверху
form.attributes("-alpha", 0.9)  # Прозрачность окна
form.attributes("-fullscreen", False)  # Не полноэкранный режим
# form.attributes("-toolwindow", True)  # Окно без кнопок управления  
# form.attributes("-disabled", False)  # Окно активно
# form.attributes("-zoomed", False)  # Не увеличенное окно
# form.attributes("-transparentcolor", "#f0f0f0")  # Цвет прозрачности
nameframe = tk.Frame(form, bg="#f0f0f0")    # создаем фрейм для имени
nameframe.pack(pady=10)  # отступ сверху
# создаем фрейм для имени и фамилии
lblname = tk.Label(nameframe, text="Имя", font=("Arial", 12), bg="#f0f0f0", fg="#000000")  # создаем метку имени
lblname.grid(row=0, column=0, padx=5)  # размещаем метку имени
lblsname = tk.Label(nameframe, text="Фамилия", font=("Arial", 12), bg="#f0f0f0", fg="#000000")  # создаем метку фамилии
lblname.grid(row=1, column=0, padx=5)  # размещаем метку фамилии
txtname = tk.Entry(nameframe, width=30, font=("Arial", 12), bg="#f0f0f0", fg="#000000")  # создаем поле ввода имени
txtname.grid(row=0, column=1, padx=5)  # размещаем поле ввода имени
txtsname = tk.Entry(nameframe, width=30, font=("Arial", 12), bg="#f0f0f0", fg="#000000")  # создаем поле ввода фамилии
txtsname.grid(row=1, column=1, padx=5)  # размещаем поле ввода фамилии
dataframe = tk.Frame(form, bg="#005500")    # создаем фрейм для данных
dataframe.pack(pady=10)  # отступ сверху
lblcity = tk.Label(dataframe, text="Город", font=("Arial", 12), bg="#005500", fg="#000000")  # создаем метку города
lblcity.grid(row=0, column=0, padx=5)  # размещаем метку города
txtcity = tk.Entry(dataframe, width=30, font=("Arial", 12), bg="#005500", fg="#000000")  # создаем поле ввода города

lblstreet = tk.Label(dataframe, text="Улица", font=("Arial", 12), bg="#005500", fg="#000000")  # создаем метку улицы
lblstreet.grid(row=1, column=0, padx=5)  # размещаем метку улицы
txtstreet = tk.Entry(dataframe, width=30, font=("Arial", 12), bg="#005500", fg="#000000")  # создаем поле ввода улицы
txtcity.grid(row=0, column=1, padx=5)  # размещаем поле ввода города
telmailframe = tk.Frame(form, bg="#000055")    # создаем фрейм для телефона и почты 
tk.mainloop()