Ejercicios

''''
Ejemplo multi hilo
mport _thread
import time

def horaActual(nombre_thread, tiempo_de_espera):
    count=0
    while count < 5:
        time.sleep(tiempo_de_espera)
        count += 1
        print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')

_thread.start_new_thread(horaActual, ("thread_uno", 1))
_thread.start_new_thread(horaActual, ("thread_dos", 2))

while True:
    pass
'''

#Logging para generar ficheros de registros
'''
import logging

logging.warning("Hace calor")
'''

''''
#Filter aplica una función a todos los elementos de una lista
numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def mifuncion(x):
    if str(x).startswith("pep"):
        return True

    return False

resultado = filter(lambda x:str(x).startswith("pep"), ["pepe", "pepito", "juan"])
print(list(resultado))
'''
''''
#Map sirve para adjudicar de manera indiscriminada los elementos de la lista si cumple la condición

def cuadrado(x):
    return x*x


resultado = map(cuadrado, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(resultado))
'''
'''
from functools import reduce
#Reduce usa de forma recurrente los elementos hasta que solo queda uno en la lista

def suma(a, b):
    return a + b

res = reduce(suma, [1, 2, 3, 4, 5])
print(res)
'''

''''
cursos = ["Java", "Python", "Git"]
asistentes = [15, 20, 4]
demo = zip(cursos, asistentes)
print(list(demo))
'''
'''
#All - Any para verificar que las condiciones de la lista se cumplen o no. Con all, si uno de los elementos es falso, imprimirá False y con any imprimirá True si al menos uno de los elementos es verdadero.

listaA = [1 == 1, 2 == 2, 3 == 4]
res = all(listaA)
print(res)
'''

#Round se usa para redondear
'''
a = 5.5
b = 5.4
c = 5.6

print(round(a))
'''