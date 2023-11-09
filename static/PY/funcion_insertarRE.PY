from static.PY.funcion_conexion import *
import mysql.connector

def insertar_variables_registro_re(fecha_e,descripcion,n_r,n_e,):
    print("estamos en la función registro usuarios")

    try:
        connection=conexion()
        if (connection):
            print("conexión realizada")


        cursor= connection.cursor()

        Query= """ INSERT INTO `registrarre`(`fecha_e`, `descripcion`, `n_r`, `n_e`) VALUES (%s,%s,%s,%s) """

        variables=(fecha_e, descripcion, n_r, n_e)  
        cursor.execute(Query, variables)     
        connection.commit()
        print("se realizo la inserción") 

    except mysql.connector.Error:
        print("algo ha fallado")

