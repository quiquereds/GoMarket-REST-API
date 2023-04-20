# Importamos la librería de Flask
from flask import Flask,jsonify, request
# Importamos el diccionario del archivo 'config.py'
from config import config
# Importamos el conector de Flask para la base de datos en MySQL
from flask_mysqldb import MySQL

# Se crea una app de Flask y es utilizada para crear una API posteriormente
app = Flask(__name__)

# Creamos el conector dando como parámetro nuestra aplicación
conector = MySQL(app)

# Método del servicio web que será de tipo GET para obtener la lista de productos
@app.route('/productos', methods=['GET'])
def getProductos():
    try:
        # Creamos un objeto cursor para interactuar con la base de datos
        cursor = conector.connection.cursor()
        # Creamos una sentencia SQL para obtener la lista de productos e la tabla Productos
        obtenerProductos = "SELECT * FROM producto"
        # Ejecutamos la sentencia creada anteriormente
        cursor.execute(obtenerProductos)
        # Capturamos los datos en una variable
        datos = cursor.fetchall()
        # Creamos una lista vacía para almacenar los productos
        productos = []
        # Recorremos cada fila de la tabla
        for fila in datos:
            # Por cada fila almacenamos los datos de cada producto en un diccionario
            producto={
                'idProducto':fila[0],
                'nombre':fila[1],
                'descripcion':fila[2],
                'precio':fila[3],
                'stock':fila[4],
                'imagen':fila[5],
            }
            # Cada que se recorra un producto lo anexamos al diccionario
            productos.append(producto)
        # Retornamos en formato JSON los datos
        return jsonify({
            'productos':productos,
            'mensaje':'Productos listados'
        })
    except Exception as e:
        return jsonify({
            'mensaje':'Ocurrió un problema...'
        }), 500 # Devolvemos código de estado de error interno del servidor

# Método del servicio web de tipo GET para obtener un producto en específico
@app.route('/productos/<codigo>', methods=['GET'])
def getProducto(codigo):
    try:
        # Creamos un objeto cursor para interactuar con la base de datos
        cursor = conector.connection.cursor()
        # Creamos una sentencia SQL para obtener el producto específico que se está indicando en la URL
        obtenerProducto = "SELECT * FROM producto WHERE idProducto = '{0}'".format(codigo)
        # Ejecutamos la sentencia creada anteriormente
        cursor.execute(obtenerProducto)
        # Capturamos el producto en una variable
        datos = cursor.fetchone()
        # Detectamos si la variable no está vacía para mostrar los datos
        if datos != None:
            producto={
                'idProducto':datos[0],
                'nombre':datos[1],
                'descripcion':datos[2],
                'precio':datos[3],
                'stock':datos[4],
                'imagen':datos[5],
            }
            # Retornamos en formato JSON el producto
            return jsonify({
                'producto':producto,
                'mensaje':'Producto encontrado'
            })
        else:
            return jsonify({
            'mensaje':'Producto no encontrado...'
        }), 404 # Devolvemos código de estado de recurso no encontrado
    except Exception as e:
        return jsonify({
            'mensaje':'Ocurrió un problema...'
        }), 500 # Devolvemos código de estado de error interno del servidor

@app.route('/productos', methods=['POST'])
def postProducto():
    try:
        # Creamos un objeto cursor para interactuar con la base de datos
        cursor = conector.connection.cursor()
        # Ejecutamos una sentencia SQL para agregar un producto a través de una petición POST del servicio web
        registrarProducto = "INSERT INTO producto (idProducto, nombre, descripcion, precio, stock, imagen) VALUES ('{0}', '{1}', '{2}', {3}, {4}, '{5}')".format(request.json['idProducto'], request.json['nombre'], request.json['descripcion'], request.json['precio'], request.json['stock'], request.json['imagen'])
        # Ejecutamos la sentencia creada anteriormente
        cursor.execute(registrarProducto)
        # Confirmamos los cambios de inserción
        conector.connection.commit()
        # Devolvemos respuesta en formato JSON
        return jsonify({
            'mensaje':'Producto agregado...', 
        }), 201 # Devolvemos código de estado de recurso creado
    except Exception as e:
        return jsonify({
            'mensaje':'Ocurrió un problema...'
        }), 
    
@app.route('/productos/<codigo>', methods=['DELETE'])
def deleteProducto(codigo):
    try:
        # Creamos un objeto cursor para interactuar con la base de datos
        cursor = conector.connection.cursor()
        # Creamos una sentencia SQL para eliminar el producto específico que se está indicando en la URL
        eliminarProducto = "DELETE FROM producto WHERE idProducto = '{0}'".format(codigo)
        # Ejecutamos la sentencia creada anteriormente
        cursor.execute(eliminarProducto)
        # Confirmamos los cambios de inserción
        conector.connection.commit()
        # Devolvemos respuesta en formato JSON
        return jsonify({
            'mensaje':'Producto eliminado...', 
        })
    except Exception as e:
        return jsonify({
            'mensaje':'Ocurrió un problema...'
        }), 500 # Devolvemos código de estado de error interno del servidor

@app.route('/productos/<codigo>', methods=['PUT'])
def putActualizarProducto(codigo):
    try:
        # Creamos un objeto cursor para interactuar con la base de datos
        cursor = conector.connection.cursor()
        # Ejecutamos una sentencia SQL para modificar un producto a través de una petición PUT del servicio web
        actualizarProducto = "UPDATE producto SET nombre = '{0}', descripcion = '{1}', precio = {2}, stock = {3}, imagen = '{4}' WHERE idProducto = '{5}'".format(request.json['nombre'], request.json['descripcion'], request.json['precio'], request.json['stock'], request.json['imagen'], codigo)
        # Ejecutamos la sentencia creada anteriormente
        cursor.execute(actualizarProducto)
        # Confirmamos los cambios de actualización
        conector.connection.commit()
        # Devolvemos respuesta en formato JSON
        return jsonify({
            'mensaje': 'Producto actualizado...',
        }), 200  # Devolvemos código de estado OK
    except Exception as e:
        return jsonify({
            'mensaje': 'Ocurrió un problema...'
        }), 500  # Devolvemos código de estado de error interno del servidor

# Creamos una función para gestionar las páginas no encontradas (Error 404)
def pagina404(error):
    # Retornamos un mensaje de error de que la página no existe
    return '<h1>Ups! Esta página no existe... </h1>', 404 # Devolvemos código de estado de recurso no encontrado

# Comprobamos si estamos ejecutando el archivo como principal
if __name__ == '__main__':
    # Leemos la configuración de la llave del diccionario 'development' del archivo ´/src/config.py´
    app.config.from_object(config['development'])
    # Configuramos la gestión de errores 404 (Página no encontrada)
    app.register_error_handler(404, pagina404)
    # Ejecutamos la aplicación
    app.run()