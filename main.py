from tkinter import *
import math as m

window = Tk()
window.title('Решение квадратных уравнений')
window.geometry('250x100')


def solution():
    d = (b.get() ** 2) - (4 * a.get() * c.get())
    if d >= 0:
        x1_label_text.set('x1=')
        x1_output.set(str((-(b.get()) + m.sqrt(d)) / (2 * a.get())))
        x2_label_text.set('x2=')
        x2_output.set(str((-(b.get()) - m.sqrt(d)) / (2 * a.get())))
    else:
        x1_label_text.set('Error')
        x1_output.set('D<0')
        x2_label_text.set('')
        x2_output.set('')



a = IntVar()
a_enter = Entry(window, textvariable=a, width=5)
a_enter.grid(row=1, column=0)

a_label = Label(window, text='x^2+')
a_label.grid(row=1, column=1, )

b = IntVar()
b_enter = Entry(window, textvariable=b, width=5)
b_enter.grid(row=1, column=2)

b_label = Label(window, text='x+')
b_label.grid(row=1, column=3)

c = IntVar()
c_enter = Entry(window, textvariable=c, width=5)
c_enter.grid(row=1, column=4)

free_label = Label(window, text='= 0')
free_label.grid(row=1, column=5)

enter_button = Button(text='Решить', command=solution, width=7)
enter_button.grid(row=1, column=6, padx=10)

x1_label_text = StringVar()
x1_label = Label(window, textvariable=x1_label_text)
x1_label.grid(row=2, column=0)

x2_label_text = StringVar()
x2_label = Label(window, textvariable=x2_label_text)
x2_label.grid(row=3, column=0)

x1_output = StringVar()
x1_enter = Label(window, textvariable=x1_output)
x1_enter.grid(row=2, column=1)

x2_output = StringVar()
x2_enter = Label(window, textvariable=x2_output)
x2_enter.grid(row=3, column=1)

error = StringVar()
error_label = Label(window, textvariable=error)
error_label.grid(row=2, column=2)

window.mainloop()
