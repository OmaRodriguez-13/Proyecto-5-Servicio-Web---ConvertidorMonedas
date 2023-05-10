import mysql.connector
import json
from flask import Flask, jsonify, request
from flask_cors import CORS

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
    password="", 
    database="conversiones"
    )

    cursor = conn.cursor()

    # Obtener la tasa de cambio de la base de datos
    cursor.execute('SELECT tasa_cambio FROM tasas_cambio WHERE moneda_origen = %s AND moneda_destino = %s', (de_moneda.upper(), a_moneda.upper()))
    row = cursor.fetchone()

    # Verificar si se encontró una tasa de cambio
    if row is None:
        # Crear un diccionario con el mensaje de error
        message = {'error': 'No se encontró una tasa de cambio para la conversión especificada'}
    else:
        # Calcular la cantidad convertida
        tasa_cambio = row[0]
        cantidad_convertida = cantidad * tasa_cambio

         # Crear un diccionario con el mensaje de respuesta
        message = {
            'cantidad': cantidad,
            'moneda_origen': de_moneda.upper(),
            'cantidad_convertida': cantidad_convertida,
            'moneda_destino': a_moneda.upper()
        }

    # Cerrar la conexión a la base de datos
    conn.close()

    # Devolver la respuesta
    return jsonify(message)

@app.route('/convertirweb/<float:cantidad2>/<de_moneda2>/<a_moneda2>')
def convertirW(cantidad2, de_moneda2, a_moneda2):
    # Conectarse a la base de datos
    conn2 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="conversiones"
    )

    cursor2 = conn2.cursor()

    # Obtener la tasa de cambio de la base de datos
    cursor2.execute('SELECT tasa_cambio FROM tasas_cambio WHERE moneda_origen = %s AND moneda_destino = %s', (de_moneda2.upper(), a_moneda2.upper()))
    row = cursor2.fetchone()

    # Verificar si se encontró una tasa de cambio
    if row is None:
        # Crear un diccionario con el mensaje de error
        message = {'error': 'No se encontró una tasa de cambio para la conversión especificada'}
    else:
        # Calcular la cantidad convertida
        tasa_cambio2 = row[0]
        cantidad_convertida2 = cantidad2 * tasa_cambio2

         # Crear un diccionario con el mensaje de respuesta
        message = {
            'cantidad': cantidad2,
            'moneda_origen': de_moneda2.upper(),
            'cantidad_convertida': cantidad_convertida2,
            'moneda_destino': a_moneda2.upper()
        }

    # Cerrar la conexión a la base de datos
    conn2.close()

    # Devolver la respuesta #return str(cantidad2) + ' ' + de_moneda2.upper() + ' equivale a ' + str(cantidad_convertida2) + ' ' + a_moneda2.upper()
    response = jsonify(message)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    app.run(host='0.0.0.0')
    #CORS(app)
    
