#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

#Primero, importamos la función reduce.

from functools import reduce

#Creamos la función
def ejercicio2(lista):
    resultado = list(filter((lambda x: x% 2), lista))
    print(resultado)
    resultado = reduce((lambda x, y: x + y), resultado)
    print(resultado)

#Generamos la lista 
lista = list(range(10))

#Imprimimos el resultado
ejercicio2(lista)