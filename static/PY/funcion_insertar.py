from static.PY.funcion_conexion import *
import mysql.connector

def insertar_variables_registro(nom,ape,id,pas,cargo):
    print("estamos en la función registro usuarios")

    try:
        connection=conexion()
        if (connection):
            print("conexión realizada")


        cursor= connection.cursor()

        Query= """ INSERT INTO `tabla_registro`(`nombre`, `apellido`, `identificacion`, `contraseña`, `cargo`) VALUES (%s,%s,%s,%s,%s) """

        variables=(nom, ape, id, pas, cargo)  
        cursor.execute(Query, variables)     
        connection.commit()
        print("se realizo la inserción") 

    except mysql.connector.Error:
        print("algo ha fallado")

def insertar_variables_registroE(nom_e, ape_e, id_e, grado):
    print("estamos en la función registro estudiantil")

    try:
        connection = conexion()
        if connection:
            print("conexión realizada")

        cursor = connection.cursor()

        Query = """INSERT INTO tabla_registro_e (nombre, apellido, identificacion, grado) VALUES (%s, %s, %s, %s)"""

        variables = (nom_e, ape_e, id_e, grado)
        cursor.execute(Query, variables)
        connection.commit()
        print("se realizo la inserción")

    except mysql.connector.Error as err:
        print(f"Algo ha fallado: {err}")
