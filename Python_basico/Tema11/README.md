# Bases de Datos y Python

Primero creamos una pequeña base de datos desde nuestra terminal para así crear una tabla en la que introduciremos algunos datos para poder trabajar con ellos.

La forma de hacerlo es la siguiente:

1) Abrimos nuestra terminal
2) Ejecutamos en la ruta que especifiquemos lo siguiente:

Ruta especificada>sqlite3 miaplicacion.db (nombre que damos a la base de datos)
SQLite version 3.38.2 2022-03-26 13:51:10
Enter ".help" for usage hints. (Con la función .help se nos mostrarán todas las opciones de SQL)
sqlite> CREATE TABLE users(
   ...> id INTEGER PRIMARY KEY,
   ...> username TEXT NOT NULL,
   ...> password TEXT NOT NULL); (Para crear la tabla usamos CREATE TABLE + nombre y entre paréntesis todos los elementos que queramos incluir. Tenemos que definir el tipo de dato y si su campo es obligatorio)
sqlite> .tables (Nos muestra las tablas que tenemos creadas)
users
sqlite> INSERT INTO users(id, username, password) VALUES(1, "lapeiro", "miclave");
sqlite> INSERT INTO users(id, username, password) VALUES(2, "jagincas","miclave");(Insertamos los datos especificando el valor para cada elemento. La Primary Key que hayamos definido ha de ser única, es decir, no admite duplicidades)
sqlite> SELECT * FROM users;(Ejecutamos un SELECT para comprobar que se ha creado todo correctamente)
1|lapeiro|miclave
2|jagincas|miclave
sqlite> .show
        echo: off
         eqp: off
     explain: auto
     headers: off
        mode: list
   nullvalue: ""
      output: stdout
colseparator: "|"
rowseparator: "\n"
       stats: off
       width:
    filename: miaplicacion.db
sqlite> .schema users (Nos muestra la estructura de nuestra tabla)
CREATE TABLE users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
password TEXT NOT NULL);
sqlite>






## Conectar la base de datos con Python

Para trabajar con Python, simplemente debemos importar sqlite3 y trabajar siguiendo el código que se especifica a continuación:

(Para conectarnos a la base de datos en Python primero  importamos sqlite3)
import sqlite3


(Definimos la variable para conectarnos a la base de datos. Especificando el nombre de la misma)
conn = sqlite3.connect("miaplicacion.db")

#Abrimos los cursores
cursor = conn.cursor()

(Hacemos la consulta)

rows = cursor.execute('SELECT * FROM users')
for row in rows:
    print(row)


(Para que funcione, todo el código debe introducirse entre la variable de conexión y la de cierre, así como el cursor)
cursor.close()
conn.close()


También podemos trabajar verificando las credenciales de usuario de la siguiente manera:

import sqlite3
import getpass

def main():
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")


def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username={username} AND password={password}"
    print("Query a ejecutar: ", query)

    rows = cursor.execute(query)
    data = rows.fetchone() #Este método nos devuelve únicamente un elemento.
    print("data es", type(data))

    cursor.close()
    conn.close()

    if __name__ == '__main__':
    main()
