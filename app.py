from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Mapa de microservicios y sus rutas
microservicios = {
    "sumar": "http://localhost:5001/Suma",
    "restar": "http://localhost:5002/Resta",
    "multiplicar": "http://localhost:5003/Multiplicacion",
    "dividir": "http://localhost:5004/Division"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['GET'])
def calculo():
    operacion = request.args.get('op')
    a = request.args.get('a')
    b = request.args.get('b')

    if operacion not in microservicios:
        return jsonify({'error': 'Operación no válida o inexistente'}), 400

    try:
        respuesta = requests.get(microservicios[operacion], params={'a': a, 'b': b})
        return jsonify(respuesta.json()), respuesta.status_code
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Error de conexión con el microservicio'}), 500

if __name__ == '__main__':
    app.run(port=5000)
