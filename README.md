# [PROYECTO5: SERVICIO WEB: CONVERSOR DE UNIDADES]

## Instalación y Configuración

### Source code

Descargar el zip que contiene los archivos fuente del proyecto.

### Vía git 

```bash
git clone https://github.com/OmaRodriguez-13/Proyecto3.1--Middleware-SECRETWORD-PYRO4-
```

## Guía Rápida

### Requerimientos

#### **Importante: Conexión a la misma red.**
#### Editor de código (por ejemplo: [Visual Studio Code]
#### Python 3.11.2
#### Pyro4:

```bash
pip install pyro4
```

### Instrucciones de uso

Cambie la linea 58 del archivo [server.py] por la ip de su equipo "servidor".
[![line58.png](https://i.postimg.cc/TPsVJVM5/line58.png)](https://postimg.cc/QBpKXWMj)

```bash
ipconfig
```

## Ejecución

### Servidor

Abra un terminal y ejecute [server.py] con alguno de los siguiente comandos:

```bash
py server.py
```

```bash
python server.py
```

El servidor devolverá la URI creada.

[![server.png](https://i.postimg.cc/0QMJWNVx/server.png)](https://postimg.cc/TLxwhT8H)

### Cliente

En otra terminal, ejecute [client.py] con alguno de los siguientes comandos:

```bash
py client.py
```

```bash
python client.py
```

En las ventanas siguientes deberá introducir la ip y el puerto del servidor, respectivamente.
[![ip.png](https://i.postimg.cc/CK9SJknZ/ip.png)](https://postimg.cc/cK7pLKmZ)
[![port.png](https://i.postimg.cc/rskc2TJM/port.png)](https://postimg.cc/0Mch7LFB)
[![client.png](https://i.postimg.cc/j5TksSGg/client.png)](https://postimg.cc/67Hhct6n)

## Testeo

### Servidor [server.py]

Introducir la palabra secreta "secretword" a adivinar (sin importar mayúsculas y minúsculas), así como la pistas de ayuda al cliente (principal y secundaria).
[![secretword.png](https://i.postimg.cc/RhjNJhwf/secretword.png)](https://postimg.cc/BPBqdqYQ)
[![principal.png](https://i.postimg.cc/dQ7R3yYh/principal.png)](https://postimg.cc/Th65Hhhx)
[![pista.png](https://i.postimg.cc/Vk5zPmMP/pista.png)](https://postimg.cc/DSV9qVBx)


### Cliente [client.py]
[![gui.png](https://i.postimg.cc/7YXwGfD2/gui.png)](https://postimg.cc/SJXwHQnS)

Ya iniciado el programa cliente, el usuario tendrá un mensaje de advertencia para que introduzca únicamente minúsculas.
[![regla.png](https://i.postimg.cc/DfXSXQYb/regla.png)](https://postimg.cc/kD7MrSCn)

El usuario tendrá 3 intentos para adivinar la palabra secreta, por cada fallo obtendrá una nueva pista.
[![intento1.png](https://i.postimg.cc/T34x0FK2/intento1.png)](https://postimg.cc/MnVgKs0g)
[![fallo.png](https://i.postimg.cc/fTHQWpj7/fallo.png)](https://postimg.cc/JGB2PTFt)

Una vez agotadas todas sus oportunidades, el usuario tendrá la opción de volver a iniciar el juego.
[![nuevo.png](https://i.postimg.cc/dQ4xGdkw/nuevo.png)](https://postimg.cc/23LGD17K)

También puede reiniciar el juego en el momento en que lo desee utilizando el botón "Volver a empezar".
[![reinicio.png](https://i.postimg.cc/5trtHjB3/reinicio.png)](https://postimg.cc/3yghV8b4)
