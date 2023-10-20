from static.PY.funcion_conexion import *

def borrar_datos(identificacion):
    print("borrar datos")
    
    try:
        connection=conexion()
        if (connection):
            print("conexión realizada")


        cursor= connection.cursor()

        Query= "DELETE FROM `tabla_registro` WHERE identificacion = %s;"

        variables=(identificacion,)  
        cursor.execute(Query, variables)     
        connection.commit()
        print("se realizo la inserción") 

    except mysql.connector.Error:
        print("algo ha fallado")
    