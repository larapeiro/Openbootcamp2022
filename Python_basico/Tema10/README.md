# **GUI**

Una interfaz gráfia de usuario es una aplicación que nos muestra de manera visual una itnerfaz que nos permite interactuar con un programa nativo o con otros programas. Un ejemplo de ello de Visual Studio Code. 

Para nuestros ejercicios haremos uso de:

- Tkinter



### Ejercicios realizados durante la sesión

Estos ejercicios son las prácticas que se han ido realizando durante la sesión de GUI 

'''
Creamos una ventana

window = tkinter.Tk()

Creamos los widgets para nuestra ventana

label_saludo = tkinter.Label(window, text="¡Hola!", bg="yellow", fg="blue")

Para posicionar la etiqueta, tenemos que hacer uso de la geometría pack

label_saludo.pack(ipadx=50, ipady=50, side='left')

label_adios = tkinter.Label(window, text="Adiós", bg="red")
label_adios.pack(ipadx=50, ipady=50)

window.mainloop()
'''
'''
Comprobar todas las funciones que tenemos
import pprint
pprint.pprint(dir(window))
'''
'''
import tkinter
from tkinter import ttk

window= tkinter.Tk()

weight indica el número de elementos que podemos introducir

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

Otra forma de crear la etiqueta es con ttk

usarname_label=ttk.Label(window, text="Username: ")

Indicamos la posición de la etiqueta. Con sticky posicionamos la etiqueta y se rige por las letras en ingles de la orientación(Norte, Oeste, Este, Sur)

usarname_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

Las entradas de texto se hacen de la siguiente manera

username_entry= ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

Hacemos lo mismo para añadir una nueva etiqueta teniendo en cuenta que debemos modificar la fila o columna

password_label=ttk.Label(window, text="Password: ")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password_entry= ttk.Entry(window, show='*') 

Con show indicamos como queremos que se muestre el texto que escribimos.

password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

A continuación, vamos a generar un botón

login_button=ttk.Button(window, text="Iniciar sesión")
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

'''

'''
import tkinter
from tkinter import ttk
import random

window= tkinter.Tk()

Podemos añadir diferentes características de manera aleatoria usando random.

colors = ["blue", "red", "yellow", "purple", "green", "black"]
for x in range(0,10):
    color= random.randint(0, len(colors)-1)
    color2= random.randint(0, len(colors)-1)
    

label1= tkinter.Label(window, text="Posicionamiento absoluto", bg=colors[color], fg=colors[color2])
label1.place(x=random.randint(0,100), y=random.randint(0,100))




window.mainloop()
'''
'''
import tkinter
from tkinter import ttk

window= tkinter.Tk()

frame= ttk.Frame(window)
label= ttk.Label(frame, text="hola")
label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)
frame.grid(column=0, row=0, sticky=tkinter.W)


window.mainloop()
'''

'''

import tkinter
from tkinter import ttk

window= tkinter.Tk()
lista = ["Windows", "macOS", "Linux", "MS DOS", "AmigaOS", "BeOS"]

listbox=tkinter.Listbox(window, height=100, listvariable=lista)
listbox.grid(column=0, row=0, sticky=tkinter.W)

window.mainloop()
''''