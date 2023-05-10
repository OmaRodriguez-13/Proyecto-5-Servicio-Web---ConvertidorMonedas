# [PROYECTO5: SERVICIO WEB: CONVERTIDOR DE MONEDAS]

## Descripción general

El proyecto consiste en la creación de un servicio web, en este caso, un convertidor de monedas desarrollado en Flask. El cual puede ser consumido (accesado) en 2 modalidades:
1. En primer lugar desde otra aplicación (programa) de escritorio (request.py).
2. Desde una página web (index.html).

## Instalación y Configuración

### Source code

Descargar el zip que contiene los archivos fuente del proyecto.

### Vía git 

```bash
git clone https://github.com/OmaRodriguez-13/Proyecto-5-Servicio-Web---ConvertidorMonedas.git
```

## Guía Rápida

### Requerimientos

- Importante: Conexión a la misma red.
- Desactivar Firewall de Windows para evitar cualquier error de conexión.
- MySQL Workbench 8.0 CE.
- Editor de código (por ejemplo: [Visual Studio Code]).
- Python 3.11.2

#### requests:

```bash
pip install requests
```

#### json:

```bash
pip install json
```

#### Flask:

```bash
pip install Flask flask-cors
```

#### MySQL Connector Python:

```bash
pip install mysql-connector-python
```

### Instrucciones de uso

Cambie la linea 135 del archivo [index.html] por únicamente la ip que tenga su equipo "servidor".
Nota: Si usará el mismo equipo para ambos casos, entonces reemplanzarlo por "127.0.0.1".

[![ipindex.png](https://i.postimg.cc/qRmhYsg0/ipindex.png)](https://postimg.cc/S2MxYzWt)

Si no conoce su dirección ip de su equipo, puede usar el siguiente comando en cmd.

```bash
ipconfig
```
### Live Server de Visual Studio Code

Buscar e instalar la extensión "Liver Server"

[![liveserver.png](https://i.postimg.cc/SQ2WCTgk/liveserver.png)](https://postimg.cc/rzT0LJ6P)

### Configuración de la base de datos

1. Importar la base de datos del archivo "import.sql".

2. En caso de no ser posible la importación de la base de datos con el método anterior, utilizar el archivo “src/TASAS DE CONVERSION.sql”:
- Utilizar o crear una nueva conexión.

[![conexion.png](https://i.postimg.cc/vThCZKq9/conexion.png)](https://postimg.cc/jnWM8Mrd)

- Ejecutar el comando para crear la base de datos “conversiones” y usarla.
- Ejecutar el comando para crear la tabla “tasas_cambio”.
- Ingresar los datos en la tabla.

2. Cambiar las líneas 18 a 21; así como 57 a 60 en el archivo [app.py] en caso de ser necesario para adecuarlo con sus permisos de administrador de la base de datos en MySQL Workbench.

[![local.png](https://i.postimg.cc/W3d06Ybg/local.png)](https://postimg.cc/qhdtpLKv)


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

Abrir la página web (index.html) dando click derecho y seleccionando la opción "Open with Live Server" de la extensión Live Server.

[![open.png](https://i.postimg.cc/d0vCptQs/open.png)](https://postimg.cc/K1q4gbgw)

En la página web, deberá introducir la cantidad a convertir, así como seleccionar las divisas correspondientes.

[![index.png](https://i.postimg.cc/bvTnhcdQ/index.png)](https://postimg.cc/DWS0rNrZ)
