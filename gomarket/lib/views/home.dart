import 'package:flutter/material.dart';
import 'package:gomarket/views/product_details.dart';
import 'package:liquid_pull_to_refresh/liquid_pull_to_refresh.dart';
import '../functions/gomarket_api.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    // Retornamos la estructura básica de una aplicación
    return Scaffold(
      // Definimos la barra superior o appbar de la app
      appBar: AppBar(
        title: const Text(
          'Go Market',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: Colors.green[800],
      ),
      // Mostramos una lista de widgets de cada producto
      body: Column(
        children: [
          Expanded(
            child: FutureBuilder<List<dynamic>>(
              // Hacemos la petición al servidor mediante la función
              future: getProductos(),
              builder: (BuildContext context,
                  AsyncSnapshot<List<dynamic>> snapshot) {
                // Si la respuesta del servidor tiene datos, mostramos la lista de productos
                if (snapshot.hasData) {
                  return LiquidPullToRefresh(
                    backgroundColor: Colors.white,
                    color: Colors.green[800],
                    height: 250,
                    onRefresh: getProductos,
                    child: ListView.builder(
                      itemCount: snapshot.data?.length,
                      itemBuilder: (BuildContext context, int index) {
                        return GestureDetector(
                          onTap: () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) => ProductDetailsScreen(
                                  producto: snapshot.data![index],
                                ),
                              ),
                            );
                          },
                          // Definimos el diseño de cada widget de la lista
                          child: ListTile(
                            title: Text(snapshot.data?[index]['nombre']),
                            subtitle:
                                Text(snapshot.data?[index]['descripcion']),
                            leading: CircleAvatar(
                              backgroundImage:
                                  NetworkImage(snapshot.data?[index]['imagen']),
                            ),
                          ),
                        );
                      },
                    ),
                  );
                  // Si la conexión al servidor presentó algún error, lo mostramos en pantalla
                } else if (snapshot.hasError) {
                  return Text('${snapshot.error}');
                } else {
                  // Si se está estableciendo conexión, mostramos un indicador de carga
                  return const CircularProgressIndicator();
                }
              },
            ),
          )
        ],
      ),
    );
  }
}
