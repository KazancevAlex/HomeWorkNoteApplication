from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

# функция создания нового файла
def new_file ():
    global file_name
    file_name = "Без названия"
    text.delete ('1.0', END)


# функция для соханения файла
def save_as ():
    out = asksaveasfile (mode='w', defaultextension='.json')
    data = text.get ('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror ("Ошибка, нелья сохранить файл")

# функция для открытия нового файла
def open_file ():
    global file_name
    inp = askopenfile (mode='r')
    if inp is None:
        return 
        file_name = inp.name
    data = inp.read ()
    text.delete ('1.0', END)
    text.insert ('1.0', data)

    
# Задание параметров окна
root = Tk ()
root.title ("Заметки")
root.geometry ("500x500")

# Создаем текстовое поле в Заметках, позволяющее делать записи 
text = Text (root, width=500, height=500)
text.pack ()

# Задание всплывающего окна menu-bar
menu_bar = Menu (root)
file_menu = Menu (menu_bar)

menu_bar.add_cascade (label="Файл", menu=file_menu)
menu_bar.add_cascade (label="Вид")
menu_bar.add_cascade (label="Помощь")
file_menu.add_command (label="Новый", command=new_file)
file_menu.add_command (label="Открыть", command=open_file)
file_menu.add_command (label="Сохранить как", command=save_as)


root.config (menu=menu_bar)
root.mainloop ()