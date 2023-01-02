'''En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

Color

Ruedas

Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

Velocidad

Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.'''

class Vehiculo():
    color = ""
    ruedas = 0
    puertas = 0

    def __init__(self, color="", ruedas=0, puertas=0):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    def caracteristicas (self):
        return f'Color: {self.color}, Ruedas: {self.ruedas}, Puertas: {self.puertas}'
    

class Coche(Vehiculo):
    def __init__(self, color="", ruedas=4, puertas=3):
        super().__init__(color, ruedas, puertas)
    def caracteristicas(self):
        return f'Características del coche: {super().caracteristicas()}'

coche_biplaza = Coche("Azul")
print("Coche pequeño: ", coche_biplaza.caracteristicas())