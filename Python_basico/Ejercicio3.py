#Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.
def imc(estatura,peso):
    return peso/estatura**2


peso= float(input("Introduce tu peso en kg: "))
estatura= float(input("Introduce tu estatura en metros: "))
indice = imc(estatura, peso)
print("Su IMC es: {0:.2f}".format(indice))