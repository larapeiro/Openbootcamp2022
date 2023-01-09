#En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

from tkinter import *

semana = Tk()
elemento = StringVar()
listbox = Listbox(semana)
for item in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Doming"]:
    listbox.insert(END, item)
    listbox.pack()
etiqueta = Label(text="Días de la semana")
etiqueta.pack()
semana.mainloop()