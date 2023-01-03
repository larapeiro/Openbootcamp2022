#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

#Primero, abrimos el fichero en modo escritura con "w"
fichero = open("ejercicio_1.txt", "w")

#A continuación, escribimos dentro del fichero.
fichero.write("Esto es un ejercicio\n")

#Cerramos el fichero
fichero.close()



