from static.PY.funcion_conexion import *

def funcionlogin(identificacion,contraseña):
    print("iniciar sesion")
    
    try:
        connection=conexion()
        if (connection):
            print("conexión realizada")


        cursor= connection.cursor()

        Query= "SELECT identifacion, contraseña from usuarios where identificacion = %s;"

        variables=(identificacion)  
        cursor.execute(Query, variables)     
        connection.commit()
        print("se realizo la inserción") 

    except mysql.connector.Error:
        print("algo ha fallado")