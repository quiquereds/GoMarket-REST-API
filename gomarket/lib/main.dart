import 'package:flutter/material.dart';
import 'package:gomarket/constants/routes.dart';
import 'package:gomarket/views/home.dart';

// Función principal para ejecutar la aplicación
void main() {
  // Realizamos la ejecución de la aplicación
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // Creamos el widget principal de la app
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // Definimos que la app utiliza el lenguaje de diseño Material3
        useMaterial3: true,
      ),
      // Se define la ruta principal de la app
      initialRoute: '/home/',
      // Se definen las rutas de navegación que incluye la app (por el momento, solo la vista de inicio)
      routes: {
        homeRoute: (context) => const HomePage(),
      },
    );
  }
}
