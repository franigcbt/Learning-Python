import math
from tkinter import * 


root = Tk()

#se pueden poner variables en el argumento text
def myClick():
    pesoVar=int(peso.get())
    alturaVar=float(altura.get())
    calculoIMC = round(pesoVar/math.pow(alturaVar, 2), 2)
    IMC = 'Su IMC es: ' + str(calculoIMC)
    clickLabel = Label(root, text=IMC)
    clickLabel.grid()


peso = Entry(root)
pesoText = Label(root, text='Ingrese su peso en KG')
altura = Entry(root)
alturaText = Label(root, text='Ingrese su altura en Metros')
myButton = Button(root, text='Calcula tu IMC', command=myClick, bg='black', fg='white')


pesoText.grid(row=0, column=0)
peso.grid(row=1, column=0)
alturaText.grid(row=2, column=0)
altura.grid(row=3, column=0)
myButton.grid(row=4, column=0)

# ---- Main Loop ---- 
root.mainloop()