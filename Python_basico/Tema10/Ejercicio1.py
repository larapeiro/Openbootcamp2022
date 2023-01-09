#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio. Al principio no tiene que haber una opción seleccionada.

from tkinter import *

#Definimos la función seleccionar para crear nuestra lista.

def seleccionar():
    etiqueta.config(text="{}".format(opcion.get()))

#Definimos a continuación la función de reinicio

def reiniciar():
    opcion.set(None)
    etiqueta.config(text="")

#Definimos las variables
window= Tk()
opcion = StringVar()
opcion.set(None)

#Generamos con la opción Radiobutton la lista

Radiobutton(window, text="Opción 1", variable=opcion, value='Opción 1', command=seleccionar).pack(anchor=W)
Radiobutton(window, text="Opción 2", variable=opcion, value='Opción 2', command=seleccionar).pack(anchor=W)
Radiobutton(window, text="Opción 3", variable=opcion, value='Opción 3', command=seleccionar).pack(anchor=W)
Radiobutton(window, text="Opción 4", variable=opcion, value='Opción 4', command=seleccionar).pack(anchor=W)

etiqueta= Label(window)
etiqueta.pack()
Button(window, text="Reiniciar selección", command=reiniciar).pack()

window.mainloop()
