from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import random
import tkinter
from tkinter import messagebox as ms
import sys

root = tkinter.Tk()
root.title('ТЫ ДАУН?')
root.geometry('700x800-650-150')
root.resizable(height=False, width=False)

def move_btn(btn):
    '''Функция двигает кнопку в левый верхний угол. '''
    x = float(random.uniform(0.1, 0.9))
    y = float(random.uniform(0.1, 0.9))
    btn.place(relx=x, rely=y)
    #btn.grid(row=x, column=y)

def click_button():
    error = 0
    while error <= 15:
        ms.showerror('SSSSSSSSSSS', 'хихихи')
        error += 1
    if error >= 15:
        sys.exit('EXIT')


logo = PhotoImage(file='C:/Users\yalf1/PycharmProjects/pythonProject7/images/chery.png')
label = ttk.Label(image=logo, compound='bottom', cursor='pirate')
label.place(relx=-0.9, rely=-0.3)


btn = ttk.Button(text='НЕТ', cursor='pirate')
btn.place(anchor=SW, relx=0.1, rely=0.8, width=135, height=65)

btn2 = ttk.Button(root, text='ДА', cursor='spider', command=click_button)
btn2.place(anchor=SE, relx=0.9, rely=0.8, width=135, height=65)


label1 = ttk.Label(text='ТЫ ДАУН?', cursor='watch', background='black', foreground='red' , font=100)
label1.place(relx=0.85, rely=0.3)

label2 = ttk.Label(text='ТЫ ДАУН?', cursor='watch', background='black', foreground='red' , font=100)
label2.place(relx=0.01, rely=0.1)


btn.bind('<Enter>', lambda x: move_btn(btn))

root.mainloop()