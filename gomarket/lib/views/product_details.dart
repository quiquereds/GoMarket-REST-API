import 'package:flutter/material.dart';

class ProductDetailsScreen extends StatelessWidget {
  const ProductDetailsScreen({super.key, required this.producto});

  final dynamic producto;

  @override
  Widget build(BuildContext context) {
    // Retornamos la estructura básica de una aplicación
    return Scaffold(
      // Definimos el diseño del appBar de la aplicación
      appBar: AppBar(
        title: Text(
          // Al título de la barra se le asigna el nombre del producto
          producto['nombre'],
          style: const TextStyle(color: Colors.white),
        ),
        backgroundColor: Colors.green[800],
      ),
      // Devolvemos un widget que permite hacer scroll
      body: SingleChildScrollView(
        child: Column(
          // Mostramos en una columna todos los detalles del producto
          children: [
            SizedBox(
              width: 500,
              height: 500,
              child: Image.network(
                producto['imagen'],
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    producto['nombre'],
                    style: const TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 24,
                    ),
                  ),
                  Text(
                    producto['descripcion'],
                    style: const TextStyle(fontSize: 16),
                  ),
                  Text(
                    'En stock ${producto['stock']}',
                    style: const TextStyle(fontSize: 16),
                  ),
                  const SizedBox(height: 16),
                  // Mostramos en una fila el precio del producto y el botón
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        '\$${producto['precio']}',
                        style: const TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 24,
                        ),
                      ),
                      // Creamos un botón para agregar un producto al carrito, aunque de momento, sin función
                      ElevatedButton(
                        onPressed: () {},
                        child: const Text('Agregar al carrito'),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
