# db/db_config.py
import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='hospital_db'
        )
        return conexion
    except Error as e:
        print("Error al conectar a MySQL:", e)
        return None
