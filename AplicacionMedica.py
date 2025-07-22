# Importamos los módulos necesarios del conector de MySQL
import mysql.connector
from mysql.connector import Error

# Definimos una función para conectarse a la base de datos
def conectar_base_datos():
    try:
        # Creamos la conexión usando los parámetros: host, usuario, contraseña y base de datos
        conexion = mysql.connector.connect(
            host='localhost',          # Dirección del servidor (localhost si es tu misma PC)
            user='root',         # Cambia esto por tu nombre de usuario en MySQL
            password='1234',  # Cambia esto por tu contraseña
            database='hospital_db'     # Nombre de la base de datos que vas a usar
        )

        # Verificamos si la conexión fue exitosa
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos 'hospital_db'")
            return conexion  # Devolvemos el objeto de conexión para usarlo luego

    # Si hay un error, lo mostramos
    except Error as e:
        print("Error al conectar a MySQL:", e)
        return None  # Devolvemos None si algo salió mal

# Verificamos que este script sea el principal que se está ejecutando
if __name__ == "__main__":
    # Intentamos conectar
    conexion = conectar_base_datos()
    
    # Si se logró la conexión, la cerramos (esto es solo una prueba)
    if conexion:
        conexion.close()

