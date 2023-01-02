#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    nombre = ""
    nota = 0

    def __init__(self, nombre="", nota=0):
        self.nombre = nombre
        self.nota = nota
    def aprobado(self):
        return self.nota > 5
    def condicion_aprobado(self):
        if self.aprobado():
            return "si"
        else:
            return "no"
    def mostrar_alumno(self):
        return f'Nombre: {self.nombre}, Nota: {self.nota}, Aprobado: {self.condicion_aprobado()}'

alumno = Alumno("Javier Perez", 7)
print("Alumno: ", alumno.mostrar_alumno())