# [PROYECTO5: SERVICIO WEB: CONVERSOR DE UNIDADES]

## Descripción general

El proyecto consiste en la creación de un servicio web, en este caso, un convertidor de monedas desarrollado en Flask. El cual puede ser consumido (accesado) en 2 modalidades:
1. En primer lugar desde otra aplicación (programa) de escritorio (request.py).
2. Desde una página web (index.html).

## Instalación y Configuración

### Source code

Descargar el zip que contiene los archivos fuente del proyecto.

### Vía git 

```bash
git https://github.com/OmaRodriguez-13/Proyecto-5-Servicio-Web---ConvertidorMonedas
```

## Guía Rápida

### Requerimientos

#### **Importante: Conexión a la misma red.**
#### MySQL Workbench 8.0 CE
#### Editor de código (por ejemplo: [Visual Studio Code]
#### Python 3.11.2
#### Pyro4:

```bash
pip install requests
```

```bash
pip install json
```

```bash
pip install Flask flask-cors
```

```bash
pip install mysql-connector-python
```

### Instrucciones de uso

Cambie la linea 58 del archivo [index.html] por únicamente la ip de su equipo que tenga su equipo "servidor".
Nota: Si usará el mismo equipo para ambos casos, entonces reemplanzarlo por "127.0.0.1".

[![line58.png](https://i.postimg.cc/TPsVJVM5/line58.png)](https://postimg.cc/QBpKXWMj)

```bash
ipconfig
```
### Live Server de Visual Studio Code

Buscar e instalar la extensión "Liver Server"

### Configuración de la base de datos

Cambiar las lineas 18 a 21 en caso de ser necesario para que coincida con sus permisos de admin de la base de datos.

## Ejecución

### Servidor

Abra un terminal y ejecute [app.py] con alguno de los siguiente comandos:

```bash
py app.py
```

```bash
python app.py
```

La terminal del servidor devolverá las direcciones ip, así como los puertos en los que este estará escuchando las peticiones.

[![app.png](https://i.postimg.cc/vm8xYqJf/app.png)](https://postimg.cc/XrhYx87Y)

### Cliente

En otra terminal, ejecute [request.py] con alguno de los siguientes comandos:

```bash
py request.py
```

```bash
python request.py
```

En la ventana siguiente deberá ingresar la ip del equipo que funciona como servidor.
[![ip.png](https://i.postimg.cc/q7rX8x9v/ip.png)](https://postimg.cc/0ztwvDkT)

## Testeo

### Servidor [server.py]

En la terminal del servidor se irán mostrando todas las solicitudes que el o los cliente(s) realicen, las cuales incluirán la ip del cliente, fecha y hora de las peticiones y los parámetros para la conversión.

[![peticiones.png](https://i.postimg.cc/htZMqdwD/peticiones.png)](https://postimg.cc/G4YvFHdV)


### Cliente [client.py]
[![request.png](https://i.postimg.cc/Y0mB17Wg/request.png)](https://postimg.cc/0Kx4sLZ2)

Ya iniciado el programa cliente, el usuario deberá introducir la cantidad a convetir usando el formato decimal, es decir (0.0). 
Posteriormente se deben de seleccionar de cada una de las listas desplegables:

1. Moneda de origen.

[![moneda1.png](https://i.postimg.cc/DZTxCKHL/moneda1.png)](https://postimg.cc/yJLhd2V8)

2. Moneda de destino.

[![moneda2.png](https://i.postimg.cc/tJrDCnTN/moneda2.png)](https://postimg.cc/Wqk0530d)

El usuario obtendrá una ventana emergente con el resultado de su conversión solicitada.

[![result.png](https://i.postimg.cc/Yqs85FTp/result.png)](https://postimg.cc/Xp9wFrVh)


### Cliente [index.html]

Abrir la página web (index.html) utilizando la extensión Live Server.

[![open.png](https://i.postimg.cc/d0vCptQs/open.png)](https://postimg.cc/K1q4gbgw)

En la página web, deberá introducir la cantidad a convertir, así como seleccionar las divisas correspondientes.

[![index.png](https://i.postimg.cc/bvTnhcdQ/index.png)](https://postimg.cc/DWS0rNrZ)
