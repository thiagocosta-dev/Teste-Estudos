from tkinter import *
from tkinter import ttk

# Window Layout
root = Tk()
root.geometry("300x400")
root.title("CALCULADORA")

# Buttons
btn1 = Button(root, text='1')
btn1.grid(column=0, row=2, padx= 5, pady=5)

btn2 = Button(root, text='2')
btn2.grid(column=1, row=2, padx= 5, pady=5)

btn3 = Button(root, text='3')
btn3.grid(column=2, row=2, padx= 5, pady=5)

btn4 = Button(root, text='4')
btn4.grid(column=0, row=3, padx= 5, pady=5)


btn5 = Button(root, text='5')
btn5.grid(column=1, row=3, padx= 5, pady=5)


btn6 = Button(root, text='6')
btn6.grid(column=2, row=3, padx= 5, pady=5)


btn7 = Button(root, text='7')
btn7.grid(column=0, row=4, padx= 5, pady=5)


btn8 = Button(root, text='8')
btn8.grid(column=1, row=4, padx= 5, pady=5)


btn9 = Button(root, text='9')
btn9.grid(column=2, row=4, padx= 5, pady=5)


btn0 = Button(root, text='0')
btn0.grid(column=0, row=5, padx= 5, pady=5)


btn_dot = Button(root, text=',')
btn_dot.grid(column=1, row=5, padx= 5, pady=5)


btn_prc = Button(root, text='%')
btn_prc.grid(column=2, row=5, padx= 5, pady=5)


root.mainloop()
