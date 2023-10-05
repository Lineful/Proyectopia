import mysql.connector

def conexion():
    connection = mysql.connector.connect(      host='localhost',
                                               database='proyecto_pia',
                                               user='root',
                                               password='')
    return connection
      