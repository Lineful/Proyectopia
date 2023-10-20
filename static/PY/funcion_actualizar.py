from static.PY.funcion_conexion import *

def actualizar_datos(identificacion,nueva_contraseña):
    print("actualizar datos")
    
    try:
        connection=conexion()
        if (connection):
            print("conexión realizada")


        cursor= connection.cursor()

        Query= "UPDATE `tabla_registro` SET `contraseña`= %s WHERE identificacion = %s;"

        variables=(nueva_contraseña,identificacion)  
        cursor.execute(Query, variables)     
        connection.commit()
        print("se realizo la inserción") 

    except mysql.connector.Error:
        print("algo ha fallado")
    