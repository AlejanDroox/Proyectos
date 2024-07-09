import sqlite3

try:
    mi_conexion=sqlite3.connect("database/Tabla")
except Exception as ex:
    print(ex)
print("Hola")