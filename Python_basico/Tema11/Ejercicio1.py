#

import sqlite3

#Nos conectamos a la db y creamos la variable del cursor
conn = sqlite3.connect("ejercicio1.db")
cursor = conn.cursor()

#A continuación, a través del cursor realizamos las diferentes acciones solicitadas en el ejercicio.
cursor.execute("CREATE TABLE Alumnos(id INT, Nombre TEXT, Apellido TEXT)")
cursor.execute("INSERT INTO Alumnos VALUES(1, 'Alberto', 'Álvarez')")
cursor.execute("INSERT INTO Alumnos VALUES(2, 'Beatriz', 'Blanco')")
cursor.execute("INSERT INTO Alumnos VALUES(3, 'Carlos', 'Carrero')")
cursor.execute("INSERT INTO Alumnos VALUES(4, 'Diana', 'Díaz')")
cursor.execute("INSERT INTO Alumnos VALUES(5, 'Esteban', 'Emperador')")
cursor.execute("INSERT INTO Alumnos VALUES(6, 'Francisca', 'Fernández')")
cursor.execute("INSERT INTO Alumnos VALUES(7, 'Gustavo', 'Galiana')")
cursor.execute("INSERT INTO Alumnos VALUES(8, 'Helena', 'Hernández')")

conn.commit()
conn.execute("SELECT * FROM Alumnos WHERE Nombre = 'Helena'")

rows = cursor.fetchall()

print(rows)

cursor.close()
conn.close()
