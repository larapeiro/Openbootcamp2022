![N|Solid](https://vlctesting.es/wp-content/uploads/2022/08/Open-Bootcamp.png)
# Tema 8
## Entrada y salida
Hasta este tema, teníamos dos maneras de escribir: declaraciones de expresión y con la función print().

### Formatear cadenas literales
En el caso del formateo de cadenas literales, comenzamos la cadena con "f" antes de las comillas de apertura. Dentro de dicha cadena con el uso de {} podemos hacer referencia a variables o valores literales. De hecho, también reciben el nombre de f-strings.

Estas expresiones pueden ir seguidas de especificadores opcionales. Un ejemplo de ello es el redondeo de Pi, ya que usando ":" tras un entero, condicionará el número mínimo de caracteres de ancho. 

import math
print(f'The value of pi is approximately {math.pi:.3f}.')
 The value of pi is approximately 3.142.



### Método format() de cadenas
El uso básico de str.format() es el siguiente:

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"

Las llaves se reemplazan con los objetos que hemos pasados por el método str.format(). En el caso de añadir una numeración dentro de las llaves, estaremos indicando su posición en la cadena.

print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam

En el caso de cadenas de caracteres de formato muy largas y que no se quieren dividir, se formatea por nombre y no por posición. Esto se consigue pasando el diccionario y usando [] para acceder a las claves. Otra opción sería pasar el diccionario “table” como argumentos por palabra clave con la anotación **:

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

### Formateo manual de cadenas
El método str.rjust() de los objetos cadena justifica a la derecha en un campo de anchura predeterminada rellenando con espacios a la izquierda. Métodos similares a este son str.ljust() y str.center(). Estos métodos no escriben nada, simplemente retornan una nueva cadena. Si la cadena de entrada es demasiado larga no la truncará sino que la retornarán sin cambios; esto desordenará la disposición de la columna que es, normalmente, mejor que la alternativa, la cual podría dejar sin usar un valor. (Si realmente deseas truncado siempre puedes añadir una operación de rebanado, como en x.ljust(n)[:n].)

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

### Leer y escribir archivos
Open() da como resultado la creación de un fichero. Suele usarse con dos argumentos de posición y una keyword de argumento.
El primer argumento es el que da nombre al archivo que se va a crear. El siguiente argumentos es una cadena que contiene los caracteres que describen la forma en que el fichero tiene usarse. Estas formas pueden ser:

-	“r”: solo de lectura
-	“w”: solo de escritura
-	“a”: para añadir al final del contenido del fichero
-	“r+”: tanto para lectura como escritura
-	“r”: si se omite el argumento, porque es opcional

Cuando se lee en modo texto, por defecto se convierten los fines de líneas que son específicos a las plataformas (\n en Unix, \r\n en Windows) a solamente \n. Cuando se escribe en modo texto, por defecto se convierten los \n a los finales de línea específicos de la plataforma. Este cambio automático está bien para archivos de texto, pero corrompería datos binarios como los de archivos JPEG o EXE. 

### Métodos de los objetos Archivo
F= fichero que ya hemos creado
Para leer el contenido de una archivo utiliza f.read(size), el cual lee alguna cantidad de datos y los retorna como una cadena de (en modo texto) o un objeto de bytes (en modo binario). size es un argumento numérico opcional. Cuando se omite size o es negativo, el contenido entero del archivo será leído y retornado; es tu problema si el archivo es el doble de grande que la memoria de tu máquina. De otra manera, como máximo size caracteres (en modo texto) o size bytes (en modo binario) son leídos y retornados. Si se alcanzó el fin del archivo, f.read() retornará una cadena vacía ('').

f.readline() lee una sola linea del archivo; el carácter de fin de linea (\n) se deja al final de la cadena, y sólo se omite en la última linea del archivo si el mismo no termina en un fin de linea. Esto hace que el valor de retorno no sea ambiguo; si f.readline() retorna una cadena vacía, es que se alcanzó el fin del archivo, mientras que una linea en blanco es representada por '\n', una cadena conteniendo sólo un único fin de linea.

 
f.write(cadena) escribe el contenido de la cadena al archivo, retornando la cantidad de caracteres escritos.

f.tell() retorna un entero que indica la posición actual en el archivo representada como número de bytes desde el comienzo del archivo en modo binario y un número opaco en modo texto.

Para cambiar la posición del objeto archivo, utiliza f.seek(offset, whence). La posición es calculada agregando el offset a un punto de referencia; el punto de referencia se selecciona del argumento whence. Un valor whence de 0 mide desde el comienzo del archivo, 1 usa la posición actual del archivo, y 2 usa el fin del archivo como punto de referencia. whence puede omitirse, el valor por defecto es 0, usando el comienzo del archivo como punto de referencia.