import 'dart:convert';
import 'package:http/http.dart' as http;

Future<List<dynamic>> getProductos() async {
  final response = await http.get(Uri.parse('http://10.0.2.2:5000/productos'));
  if (response.statusCode == 200) {
    return json.decode(response.body)['productos'];
  } else {
    throw Exception('Ups! No se pueden cargar los productos');
  }
}

Future<dynamic> getProducto(String codigo) async {
  final response =
      await http.get(Uri.parse('http://10.0.2.2:5000/productos/$codigo'));
  if (response.statusCode == 200) {
    return json.decode(response.body)['producto'];
  } else {
    throw Exception('Ups! No puedo mostrarte el producto');
  }
}
