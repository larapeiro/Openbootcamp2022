#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

#Primero importamos del módulo pickle las funciones de dump y load
from pickle import dump, load

#Creamos la clase de Vehículo
class Vehiculo:
    def __init__(self, marca, puertas, ruedas):
        self.marca = marca
        self.puertas = puertas
        self.ruedas = ruedas
    def __str__(self):
        return f"Marca: {self.marca} Puertas: {self.puertas} Ruedas: {self.ruedas}"

#A continuación, definimos el objeto de la clase
coche = Vehiculo("Ford", 3, 4)
print(coche)

#Creamos el fichero donde se almacenará el objeto que hemos creado anteriormente de tipo Vehículo con la funcion open y dump
fichero = open("fichero_2.txt", "wb+")
dump(coche, fichero)

#Cerramos el fichero
fichero.close()

#Por último, cargamos el fichero mediante la función load
fichero = open("fichero_2.txt", "rb")
datos = load(fichero)
fichero.close()

print("Muestrame los datos del vehículo: ", datos)