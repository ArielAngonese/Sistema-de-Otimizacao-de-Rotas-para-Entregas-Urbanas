from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_all_deliveries

# Criação da aplicação Flask
app = Flask(__name__)
CORS(app)

# Rota para obter todas as entregas
@app.route("/deliveries", methods=["GET"])
def get_deliveries():
    deliveries = get_all_deliveries()
    return jsonify(deliveries)