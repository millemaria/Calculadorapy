from tkinter import *
from tkinter import ttk

cor1 = "#3b3b3b"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=50, bg=cor1)
frame_corpo.grid(row=1, column=0)

valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Arial', 18), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

def entrar_valores():
    resultado = eval('9/9')
    valor_texto.set(resultado)

b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_1.grid(row=0, column=0)

b_2 = Button(frame_corpo, command=valor_texto, text="%", width=5, height=2, bg=cor4, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_2.grid(row=0, column=1)
b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_3.grid(row=0, column=2)

b_4 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_4.grid(row=1, column=0)
b_5 = Button(frame_corpo, text="8", width=5, height=2, bg=cor4, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_5.grid(row=1, column=1)
b_6 = Button(frame_corpo, text="9", width=5, height=2, bg=cor4, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_6.grid(row=1, column=2)
b_7 = Button(frame_corpo, text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_7.grid(row=1, column=3)

b_8 = Button(frame_corpo, text="4", width=5, height=2, bg=cor4, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_8.grid(row=2, column=0)
b_9 = Button(frame_corpo, text="5", width=5, height=2, bg=cor4, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_9.grid(row=2, column=1)
b_10 = Button(frame_corpo, text="6", width=5, height=2, bg=cor4, fg=cor2, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_10.grid(row=2, column=2)
b_11 = Button(frame_corpo, text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_11.grid(row=2, column=3)

b_12 = Button(frame_corpo, text="1", width=5, height=2, bg=cor5, fg=cor4, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_12.grid(row=3, column=0)
b_13 = Button(frame_corpo, text="2", width=5, height=2, bg=cor5, fg=cor4, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_13.grid(row=3, column=1)
b_14 = Button(frame_corpo, text="3", width=5, height=2, bg=cor5, fg=cor4, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_14.grid(row=3, column=2)
b_15 = Button(frame_corpo, text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_15.grid(row=3, column=3)

b_16 = Button(frame_corpo, text="0", width=5, height=2, bg=cor5, fg=cor2, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_16.grid(row=4, column=0)
b_17 = Button(frame_corpo, text=".", width=5, height=2, bg=cor5, fg=cor2, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_17.grid(row=4, column=1)
b_18 = Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Arial', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
b_18.grid(row=4, column=2)

janela.mainloop()