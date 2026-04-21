from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_all_deliveries, get_delivery_by_id

# Criação da aplicação Flask
app = Flask(__name__)
CORS(app)

# Rota para obter todas as entregas
@app.route("/deliveries", methods=["GET"])
def get_deliveries():
    deliveries = get_all_deliveries()
    return jsonify(deliveries)

# Rota para obter uma entrega específica por ID
@app.route("/deliveries/<int:id>", methods=["GET"])
def get_delivery(id):
    delivery = get_delivery_by_id(id)
    if delivery is None:
        return jsonify({"erro": "Entrega não encontrada"}), 404
    return jsonify(delivery)