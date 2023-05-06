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

### Configuración de la base de datos


## Ejecución

### Servidor

Abra un terminal y ejecute [app.py] con alguno de los siguiente comandos:

```bash
py app.py
```

```bash
python app.py
```

La terminal del servidor devolverá las direcciones ip así como los puertos en los que este estará escuchando las peticiones.

[![server.png](https://i.postimg.cc/0QMJWNVx/server.png)](https://postimg.cc/TLxwhT8H)

### Cliente

En otra terminal, ejecute [request.py] con alguno de los siguientes comandos:

```bash
py request.py
```

```bash
python request.py
```

En la ventana siguiente deberá ingresar la ip del equipo que funciona como servidor.
[![ip.png](https://i.postimg.cc/CK9SJknZ/ip.png)](https://postimg.cc/cK7pLKmZ)
[![client.png](https://i.postimg.cc/j5TksSGg/client.png)](https://postimg.cc/67Hhct6n)

## Testeo

### Servidor [server.py]

En la terminal del servidor se irán mostrando todas las solicitudes que el o los cliente(s) realicen.



### Cliente [client.py]
[![gui.png](https://i.postimg.cc/7YXwGfD2/gui.png)](https://postimg.cc/SJXwHQnS)

Ya iniciado el programa cliente, el usuario deberá introducir la cantidad a convetir usando el formato decimal, es decir (0.0). 
Posteriormente se deben de seleccionar de cada una de las listas desplegables:

1. Moneda de origen.
2. Moneda de destino.

[![regla.png](https://i.postimg.cc/DfXSXQYb/regla.png)](https://postimg.cc/kD7MrSCn)

El usuario obtendrá una ventana emergente con el resultado de su conversión solicitada.
[![intento1.png](https://i.postimg.cc/T34x0FK2/intento1.png)](https://postimg.cc/MnVgKs0g)
[![fallo.png](https://i.postimg.cc/fTHQWpj7/fallo.png)](https://postimg.cc/JGB2PTFt)

### Cliente [index.html]
