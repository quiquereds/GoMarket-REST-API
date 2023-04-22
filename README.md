<h1 align="center">
  <br>
  <a href="https://www.youtube.com/@MAPENTech/videos"><img src="https://user-images.githubusercontent.com/70863031/233258047-464e98c7-b3a7-4cc8-a31a-9bd5a13274d1.png" alt="MAPENBot - Discord Bot"></a>
  <br>
  GOMARKET RESTful API y app móvil escrita con Flutter
  <br>
</h1>

<h4 align="center">Ejemplo de servicio web tipo REST creado con Python y Flask usando los métodos HTTP GET, POST, PUT Y DELETE</h4>
<h4 align="center">Consumo de la API a tráves del método GET desde una aplicación móvil básica creada con Flutter</h4>

---
| ⚠️ | Este servicio web fue creado para un proyecto de la universidad, por lo que no es apto para su implementación en producción debido a potenciales vulnerabilidades, la creación de este repositorio es con fines educativos |
| :--------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## <img align="left" alt="Eyes" width="35px" style="padding-right:10px;" src="https://user-images.githubusercontent.com/70863031/214644849-1240d6f2-329f-46a9-8bc4-458d3d215ef8.gif"/> Descripción
Servicio web desarrollado en Python junto con el framework de Flask que incluye los métodos GET, POST, PUT Y DELETE para el intercambio de mensajes. La API proporciona acceso a una base de datos de productos creada con MySQL Workbench, los endpoints o rutas de la aplicación permiten al usuario realizar solicitudes para obtener información de los productos almacenados, añadir productos a la base de datos, modificarlos o eliminarlos, estas funciones pueden probarse utilizando herramientas de testeo de servicios web tales como Postman, Insomnia o soluciones integradas de editores de código como ThunderClient.

Para el intercambio de mensajes, se utiliza el formato JSON tanto en las respuestas del servidor al cliente y en el envío de información para la modificación de la base de datos.

Este repositorio también incluye el código de una aplicación móvil básica creada con Flutter, la cual utiliza la API del servicio web creado para mostrar los productos almacenados en la base de datos utilizando el método GET creado en la aplicación de Flask. Esta aplicación incluye una pantalla de inicio en donde se muestra la lista de productos y la página de detalles del producto seleccionado.

Este repositorio está alojado con fines educativos y el proyecto no debería ponerse en producción debido a las vulnerabilidades que tiene (a menos que decidas clonar el repositorio y mejorar el proyecto), el objetivo de este repositorio, es mostrar con fines educativos cómo se puede construir una API y consumirla desde una app, en este caso, escrita con Flutter

---

## <img align="left" alt="Rocket" width="35px" style="padding-right:10px;" src="https://user-images.githubusercontent.com/70863031/233245995-4b1c384b-ce46-49a4-b40a-4c74754ea23b.gif"/> ¿Cómo clonar el repositorio?

Para clonar este repositorio y lograr compilar este proyecto de forma local en tu computadora necesitas lo siguiente:

### 📋 Requisitos
* Tener instalado Flutter (versión 2.5.0 o superior) y Dart SDK (versión 2.14.0 o superior)
> ⚠️ Para instalar Flutter se te pueden solicitar otros recursos como tener Visual Studio, paquetes de Android Studio y el SDK de Java. Puedes verificar si necesitas instalar otros recursos y herramientas usando `flutter doctor` en la terminal.
* Tener instalado Android Studio con un respectivo emulador de dispositivo Android para compilar y probar la app 
* Tener un editor de código o IDE compatible con Flutter
> ✅ Puedes utilizar Android Studio, XCode o Visual Studio Code
* Tener un editor de código o IDE compatible con Python
> ✅ Puedes utilizar Visual Studio Code, PyCharm, Atom, etc.
* Tener instalado Python (versión 3.7 o superior)
* Tener instalado Flask (versión 2.0.1 o superior)
* Tener instalado MySQL Workbench con una conexión de base de datos
* De preferencia, alguna herramienta de testeo de servicios web como Postman para probar los métodos GET, POST, PUT y DELETE del proyecto de Flask ya que la app de Flutter solo utiliza el método GET.

### 👨‍💻 Preparación del entorno

#### Preparación del servicio web
Primero, clona este repositorio y accede al directorio del proyecto:
```bash
git clone https://github.com/quiquereds/GoMarket-REST-API.git
cd GoMarket-REST-API
```
Una vez que estés dentro del directorio del proyecto, ábrelo usando tu IDE favorito, con VS Code puedes usar:
```bash
code .
```
Dentro del proyecto, a nível raíz, abre una terminal y crea un entorno virtual de Python:
```bash
python -m virtualenv env
```
Ejecuta el script para activar el entorno:
```bash
.\env\Scripts\activate
```
Instala los paquetes necesarios del servicio web que están en el archivo `requirements.txt` mediante el comando `pip install <paquete>`, para más fácil, puedes usar:
```bash
pip install -r requirements.txt
```
Dentro de la carpeta `src` crea un archivo de Python llamado `env.py`, dentro de este, define las variables de entorno que usará el servicio web para conectarse con la base de datos que vas a utilizar (estos datos los vas a obtener dentro de MySQL Workbench), el formato debe ser el siguiente:
```python
SQL_HOST = '<Reemplaza con el host que usas en mySQL>' 
SQL_USER = '<Reemplaza con el tipo de usuario que usarás en mySQL>'
SQL_PASSWORD = '<Reemplaza con tu contraseña de conexión a mySQL>'
SQL_DB = '<Reemplaza con la base de datos que usarás en mySQL>'
```
Como recurso adicional, dentro de la carpeta `database` encontrarás un script de sentencia SQL que puedes ejecutar en MySQL Workbench para recrear la base de datos utilizada en este proyecto al igual que los datos utilizados en formato csv.

Con estos pasos, deberías poder ejecutar la aplicación de Flask y lograr que el servidor se ejecute de forma local en tu computadora.

--

#### Preparación de la app de Flutter
Primero accede al directorio del proyecto de Flutter desde la carpeta raíz:
```bash
cd gomarket
```
Instala las dependencias necesarias del proyecto a tráves de la terminal:
```bash
flutter pub get
```
Configura la dirección del servicio web dentro del archivo `lib/functions/gomarket_api.dart`:
```dart
Future<List<dynamic>> getProductos() async {
  final response = await http.get(Uri.parse('http://direccion_de_tu_servicio_web/productos'));
  if (response.statusCode == 200) {
    return json.decode(response.body)['productos'];
  } else {
    throw Exception('Ups! No se pueden cargar los productos');
  }
}
```
> ⚠️ Si estas ejecutando la aplicación de Flutter utilizando un emulador de Android y el servicio web lo estás ejecutando de forma local, deberás utilizar como dirección 10.0.2.2 en lugar de 127.0.0.1 para permitir que la aplicación acceda a los recursos de tu computadora en donde se ejecuta el servidor de Flask, por otro lado, si estás ejecutando la aplicación en un dispositivo físico, deberás indicar la dirección IP local de tu computadora en la red a la que estén ambos dispositivos (la app, en este caso el móvil y la computadora donde estás ejecutando el servicio).

Y listo, con estos pasos deberías poder compilar la aplicación y visualizarla en el emulador de Android Studio, si deseas probar la aplicación desde un dispositivo físico, será necesario que mantengas tu teléfono conectado a la computadora, habilites las opciones de desarrollador y actives el modo de DEBUG.
  
---
 
### <img align="left" alt="Rocket" width="35px" style="padding-right:10px;" src="https://user-images.githubusercontent.com/70863031/215303334-56d6d712-055a-4704-ab00-2a8d9538e974.gif"/> Lenguajes y herramientas utilizadas 

<img align="left" alt="https://www.python.org/" width="50px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/>
<img align="left" alt="https://www.python.org/" width="50px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dart/dart-original.svg"/>
<img align="left" alt="https://www.python.org/" width="50px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"/>
<img align="left" alt="https://www.mysql.com/products/workbench/" width="50px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"/>
<img align="left" alt="https://flutter.dev/" width="50px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flutter/flutter-original.svg"/>

