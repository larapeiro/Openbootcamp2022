#En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
#En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.

#Primero importamos el modulo time
import time

#A continuación, definimos la hora actual. Para ello usamos la sintaxis de strftime obteniendo la representación del objeto que indiquemos. En este caso serán horas y minutos.
hora = time.strftime("%H")
minutos = time.strftime("%M")

#El siguiente paso es comprobar si la hora es superior a las 19:00. Si se cumple la condición, por pantalla indicaremos que "Tu jornada de trabajo ha finalizado". Si por el contrario, aún quedan horas de trabajado, mostraremos un mensaje indicando un cotnador de hroas restantes.

if int(hora) >= 19:
    print ("Tu jornada laboral ha finalizado.")
else:
    print("Quedan {} horas y {} minutos para que finalice tu jornada laboral".format(19- int(hora), 59-int(minutos)))
    
