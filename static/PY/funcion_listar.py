from static.PY.funcion_conexion import *
import mysql.connector

def funcionlistar():
    print("FUNCION LISTAR")
    
    try:
        connection = conexion()
        if connection:
            print("conexión realizada")

        cursor = connection.cursor()

        query = "SELECT * FROM `tabla_registro_e`"
     
        cursor.execute(query)

        results = cursor.fetchall()

        connection.commit()

        return results



    except mysql.connector.Error as error:
        print(f"Algo ha fallado: {error}")
        return False