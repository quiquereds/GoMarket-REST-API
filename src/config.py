from env import *

# Creamos una clase con las configuraciones de desarrollo
class DevelopmentConfig():
    # Habilitamos el modo de depuración para que el servidor escuche y actualice los cambios de forma automática
    DEBUG = True
    # Establecemos los parámetros de conexión con MySQL
    MYSQL_HOST = SQL_HOST # Reemplaza con el host que usas en mySQL
    MYSQL_USER = SQL_USER # Reemplaza con el tipo de usuario que usarás en mySQL
    MYSQL_PASSWORD = SQL_PASSWORD # Reemplaza con tu contraseña de conexión a mySQL
    MYSQL_DB = SQL_DB # Reemplaza con la base de datos que usarás en mySQL

# Creamos un diccionario en donde a la llave 'development' se le asigne el valor de la clase DevelopmentConfig
config = {
    'development': DevelopmentConfig
}