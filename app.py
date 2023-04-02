import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bienvenido a la conversión de monedas'



@app.route('/convertir/<float:cantidad>/<de_moneda>/<a_moneda>')
def convertir(cantidad, de_moneda, a_moneda):
    # Conectarse a la base de datos
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MalaMedicina5",
    database="conversiones"
    )

    cursor = conn.cursor()

    # Obtener la tasa de cambio de la base de datos
    cursor.execute('SELECT tasa_cambio FROM tasas_cambio WHERE moneda_origen = %s AND moneda_destino = %s', (de_moneda.upper(), a_moneda.upper()))
    row = cursor.fetchone()

    # Verificar si se encontró una tasa de cambio
    if row is None:
        return 'No se encontró una tasa de cambio para la conversión especificada'

    # Calcular la cantidad convertida
    tasa_cambio = row[0]
    cantidad_convertida = cantidad * tasa_cambio

    # Cerrar la conexión a la base de datos
    conn.close()

    # Devolver la respuesta
    return str(cantidad) + ' ' + de_moneda.upper() + ' equivale a ' + str(cantidad_convertida) + ' ' + a_moneda.upper()

if __name__ == '__main__':
    app.run()