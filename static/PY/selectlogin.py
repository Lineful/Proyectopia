from static.PY.funcion_conexion import *
import mysql.connector

def funcionlogin(identificacion, contraseña):
    print("iniciar sesion")
    
    try:
        connection = conexion()
        if connection:
            print("conexión realizada")

        cursor = connection.cursor()

        query = "SELECT identificacion, contraseña FROM tabla_registro WHERE identificacion = %s AND contraseña = %s;"
        variables = (identificacion, contraseña)
        cursor.execute(query, variables)

        results = cursor.fetchall()

        if results:
            return True
        else:
            return False

    except mysql.connector.Error as error:
        print(f"Algo ha fallado: {error}")
        return False